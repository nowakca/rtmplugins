#!env/bin/python

# Run this from the rtmplugins directory if needed
# PYTHONPATH=. ./bin/finger.py  -s test1

import json
import requests
from argparse import ArgumentParser
from bin_utils import get_master_config, post_response


################################################################################
# Prepare our command line option reader
parser = ArgumentParser()
parser.add_argument(
    '-s',
    '--shortid',
    help='shortid of user to lookup.',
    metavar='shortid'
)
args = parser.parse_args()


#
def fetch_info(shortid):
    '''
    Given a shortid, return an object representation of its response
    '''
    api_url = 'https://jsonplaceholder.typicode.com/todos/1'
    headers = {}

    response = requests.get(api_url, headers=headers)
    # print(repr(response))

    if response.status_code == 200:
        dict = json.loads(response.content.decode('utf-8'))
        # print(dict['title'])
        return dict
    else:
        return None


################################################################################
shortid = args.shortid
post_response('DHWMC8L3D', repr(fetch_info(shortid)))
