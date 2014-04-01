#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2
import json
import sys


url = 'http://jsonip.com'
json_key = 'ip'

# don't worry too much. just expect a valid response
# and print an ugly error message otherwise ;)
try:
    handler = urllib2.urlopen(url)
    response = handler.read()
    handler.close()

    response = json.loads(response)
    print response[json_key]

except Exception as e:
    print e
    sys.exit(1)

