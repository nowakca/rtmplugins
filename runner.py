#!env/bin/python
from argparse import ArgumentParser
import sys
import os
import re
import yaml
import subprocess

from rtmbot import RtmBot

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
        try:
            bytes_res = subprocess.check_output(
                ["lpass", "show", "--notes", lk])
            string_res = str(bytes_res, 'utf-8')

            p = re.compile('(xoxb-[A-Za-z0-9-]+)')
            m = p.search(string_res)
            if m:
                config['SLACK_TOKEN'] = m.group(1)
            else:
                raise Exception(
                    'Was able to read note "{}", but could not find an xoxb- token in it.'.format(lk))
        except subprocess.CalledProcessError:  # as e:
            #print( repr(e) )
            print('Unable to read the xoxb token from "{}"'.format(lk))
            sys.exit(0)

    # Create our bot and move on
    bot = RtmBot(config)
    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit(0)
    print("Bot stopped.")


if __name__ == "__main__":
    main()
