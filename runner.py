#!env/bin/python
from argparse import ArgumentParser
import sys
import os
import yaml

from rtmbot import RtmBot
from lpass.get_lpcred import get_lpcred

'''
This is modelled on https://github.com/slackapi/python-rtmbot/blob/master/rtmbot/bin/run_rtmbot.py
It just adds in some bits to pull credentials from something other than a local text file
'''


sys.path.append(os.getcwd())


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        '-c',
        '--config',
        help='Full path to config file.',
        metavar='path'
    )
    return parser.parse_args()


def main(args=None):
    # load args with config path if not specified
    if not args:
        args = parse_args()

    # Get our base configuration info
    config = yaml.load(open(args.config or 'rtmbot.conf', 'r'))

    # overlap it with our LastPass info if needed
    lk = config['LASTPASS_KEY']
    if lk:
        config['SLACK_TOKEN'] = get_lpcred(lk, 'xoxb')

    # Create our bot and move on
    bot = RtmBot(config)
    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit(0)
    print("Bot stopped.")


if __name__ == "__main__":
    main()
