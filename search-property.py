#!/usr/bin/env python3

from common import get_pat, HttpClient
from urllib.parse import urlencode
import sys
import json

if 3 != len(sys.argv):
    print('Usage: %s FIELD VALUE' % (sys.argv[0]))
    exit(1)

search_field = sys.argv[1]
search_value = sys.argv[2]

METRY_PAT = get_pat()
client = HttpClient(METRY_PAT)
query_string = urlencode({'property.' + search_field: search_value})
response = client.get('/api/2.0/trees?%s' % (query_string))

if 200 == response.code:
    print(json.dumps(response.body_dict, indent=4))
else:
    print(response.debug_message())
