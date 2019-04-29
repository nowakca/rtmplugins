#!env/bin/python
# Add our parents path to the include path explicitly
#   (this avoids the problems with relative paths above parent)
import os
import sys
import yaml
from pathlib import Path
from slackclient import SlackClient

# I don't love this, but it seemst to be the only way to get the lpass
# module without installing it globally... and it's not near ready
# to be its own thing yet
sys.path.append(str(Path(__file__).resolve().parents[1]))
from lpass.get_lpcred import get_lpcred


# Read our config file so we can get the past to our lastpass info
config = yaml.load(open('rtmbot.conf', 'r'))
lk = config['LASTPASS_KEY']
slack_token = get_lpcred(lk, 'xoxb')


# Use the stored slack token to make a web api connection for our responses
sc = SlackClient(slack_token)
sc.api_call(
    "chat.postMessage",
    channel="DHWMC8L3D",
    text='''
:information_source:
Available commands:

`yfinger <shortid>`
  - _get Yanis info for <shortid>_

`help`
  - _shows this help_
'''
)
