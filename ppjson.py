#!/usr/bin/env python

import argparse
import json
import requests


def check_positive(value):
    ivalue = int(value)
    if ivalue < 1:
        raise argparse.ArgumentTypeError(
            "%s is an invalid positive int value" % value)
    return ivalue

parser = argparse.ArgumentParser(
    description='Grab json from an API and format it nicely')
parser.add_argument(
    'url',
    help='URL to grab json from'
)
parser.add_argument(
    '-i', '--indent',
    help='<Optional> Indent size',
    type=check_positive,
    required=False,
    default=2
)
parser.add_argument(
    '-H', '--header',
    help='<Optional> HTTP header (multiple -H arguments are allowed)',
    required=False,
    action='append',
    default=[]
)
args = parser.parse_args()


headers = {}
for h in args.header:
    headers[h.split(':')[0].strip()] = h.split(':')[1].strip()

res = requests.get(args.url, headers=headers)
res_json = res.json()
print(json.dumps(res_json, indent=args.indent))
