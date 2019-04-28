from rtmbot.core import Plugin
import pprint
import subprocess

'''
Refer to https://github.com/slackapi/python-rtmbot for Plugin documentation

Channel types:
Starts with D -> Direct Message
Starts with G -> Public or Private Channel
'''


class RepeatPlugin(Plugin):
    def __init__(self, slack_client, plugin_config):
        super().__init__(self, slack_client, plugin_config)
        self.pp = pprint.PrettyPrinter(indent=4)

    def process_message(self, data):
        '''
        Note: data['team_id'] is not defined when a sim_event is passed in.
          (The group_joined event doesn't provide it, so we can't emulate it)

        Note: subtype 'message_changed' happens on an edit
          This will have a message and previous_message object
        '''
        print('---')
        self.pp.pprint(data)
        print('\n')

        output = subprocess.check_output(["ls", "-1"])
        print(output.decode("utf-8"))

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
        # self.pp.pprint(data)
        # print('\n')
        pass
