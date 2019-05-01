#!env/bin/python

# Run this from the rtmplugins directory if needed
# PYTHONPATH=. ./bin/help_all.py

from argparse import ArgumentParser
from bin_utils import get_master_config, post_response


################################################################################
# Prepare our command line option reader
parser = ArgumentParser()
parser.add_argument(
    '-s',
    '--shortid',
    help='shortid of user to lookup',
    metavar='shortid'
)
parser.add_argument(
    '-c',
    '--channelid',
    help='id of channel to respond to',
    metavar='channelid'
)
args = parser.parse_args()


################################################################################
#
post_response(args.channelid, '''
:information_source:
Available commands:

`yfinger <shortid>`
  - _get Yanis info for <shortid>_

`help`
  - _shows this help_
''')
