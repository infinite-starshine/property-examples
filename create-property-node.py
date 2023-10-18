#!/usr/bin/env python3

from common import get_pat, HttpClient
import sys

if 2 != len(sys.argv):
    print('Usage: %s PARENT_NODE_ID' % (sys.argv[0]))
    exit(1)

parent_node = sys.argv[1]

METRY_PAT = get_pat()
client = HttpClient(METRY_PAT)
response = client.post('/api/2.0/trees', {
    'parent': parent_node,
    'name': 'My Property',
    'type': 'property',
    'property': {
        'address': 'Test Street 42',
        'property_designation': 'TEST 4:2',
    },
})

if 200 == response.code:
    print(response.body_dict['data']['_id'])
else:
    print(response.debug_message())
