import yaml
from creds.lpass import get_lpcred
from slackclient import SlackClient


def get_master_config():
    '''
    Handy way to get our base config options
    '''
    config = yaml.load(open('rtmbot.conf', 'r'))
    return config


def post_response(channel, message_content, config=None):
    '''
    Given a config that has a reference to our credentials, 
      a channel_id, and message content, posts that content to the channel.
    '''
    # Get a config if we need one
    if config == None:
        config = get_master_config()

    # Read our config file so we can get the past to our lastpass info
    lk = config['LASTPASS_KEY_WEB']
    slack_token = get_lpcred(lk, 'xoxp')

    # Use the stored slack token to make a web api connection for our responses
    sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=message_content
    )
