#!env/bin/python
import os
from slackclient import SlackClient
from lpass.get_lpcred import get_lpcred
import yaml

config = yaml.load(open('rtmbot.conf', 'r'))
#print(config)

lk = config['LASTPASS_KEY']
#print(lk)

slack_token = get_lpcred(lk, 'xoxb')
sc = SlackClient(slack_token)

sc.api_call(
    "chat.postMessage",
    channel="DHWMC8L3D",
    text="Hello from Python! :tada:"
)
