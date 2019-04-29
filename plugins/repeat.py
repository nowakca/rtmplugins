from rtmbot.core import Plugin
import pprint
import subprocess
import asyncio
import logging
from slackclient import SlackClient
from lpass.get_lpcred import get_lpcred

'''
Refer to https://github.com/slackapi/python-rtmbot for Plugin documentation

Channel types:
Starts with D -> Direct Message
Starts with G -> Public or Private Channel

This reads the LastPass Note Path from rtmbot.conf
It reads the LastPass secure note and regex extracts the token type from the text of the note

Sample Section of hte rtmbot.conf file
---
RepeatPlugin:
    web_api_path: Shared-FEBot/febot_token_web
'''

PP = pprint.PrettyPrinter(indent=4)


class RepeatPlugin(Plugin):
    def __init__(self, slack_client, plugin_config):
        '''
        After we do our base initialization, work out our identity
        so we can learn to ignore our own posts so we don't trigger ourselves.
        '''
        super().__init__(self, slack_client, plugin_config)
        self.load_rtm_info(plugin_config)
        self.load_web_info(plugin_config)

    def load_rtm_info(self, plugin_config):
        '''
        Get our basic user information that is accessible via the RTM API
          (returns our basic user id)
        '''
        at_resp = self.slack_client.api_call('auth.test')
        self.user = at_resp['user']
        self.user_id = at_resp['user_id']

    def load_web_info(self, plugin_config):
        '''
        Get our basic user information that is accessible via the Web API
          (returns our profile info)
          (also sets up 'wsc' as the web slack client interface as we need it)
        '''
        if (plugin_config['web_api_path']):
            lpcred = get_lpcred(plugin_config['web_api_path'], 'xoxp')
        else:
            raise Exception(
                'web_api_path not defined in the plugin_config for this plugin')

        self.wsc = SlackClient(lpcred)
        u_info = self.wsc.api_call('users.profile.get', user=self.user_id)
        self.bot_id = u_info['profile']['bot_id']
        # print(u_info['profile'])

        logging.info('User {} with id {} running on botid {}'.format(
            self.user, self.user_id, self.bot_id))

    ################################################################################
    # Process functions

    def process_message(self, data):
        '''
        Note: data['team_id'] is not defined when a sim_event is passed in.
          (The group_joined event doesn't provide it, so we can't emulate it)

        Note: subtype 'message_changed' happens on an edit
          This will have a message and previous_message object
        '''
        PP.pprint(data)

        # Ignore our own messages
        if 'bot_id' in data:
            if self.bot_id == data['bot_id']:
                logging.info('ignoring my own post')
                return

        output = subprocess.check_output(["./client_test.py"])
        # print(output.decode("utf-8"))

        if data['channel'].startswith("D"):
            self.outputs.append(
                [data['channel'], 'from repeat1 "{}" in channel {}'.format(
                    data['text'], data['channel']
                )]
            )
            self.outputs.append([data['channel'], output.decode("utf-8")])

    def process_member_joined_channel(self, data):
        pass

    def process_hello(self, data):
        pass

    def process_pong(self, data):
        pass

    def process_user_typing(self, data):
        pass

    def process_desktop_notification(self, data):
        pass

    def process_group_left(self, data):
        pass

    def process_group_joined(self, data):
        '''
        Called when the bot joins a channel.
        data['channel']['latest'] is a full message object (which can be passed to process_message)

        So we take that message, apply anything else we can to simulate a "proper" message,
        and we send it through processing like normal. 
        '''
        if data['channel'] and data['channel']['latest']:
            sim_event = data['channel']['latest']
            sim_event['subtype'] = 'sim_onjoin'
            sim_event['channel'] = data['channel']['id']
            sim_event['event_ts'] = sim_event['ts']
            self.process_message(sim_event)

    def catch_all(self, data):
        '''
        Uncomment this stuff when you're looking for an event that you're not seeing already
        '''
        # print('###')
        # PP.pprint(data)
        # print('\n')
        pass
