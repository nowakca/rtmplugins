#!env/bin/python

# Run this from the rtmplugins directory if needed
# PYTHONPATH=. ./bin/help_all.py

from bin_utils import get_master_config, post_response
from creds.lpass import get_lpcred
from slackclient import SlackClient


#
post_response('DHWMC8L3D', '''
:information_source:
Available commands:

`yfinger <shortid>`
  - _get Yanis info for <shortid>_

`help`
  - _shows this help_
''')
