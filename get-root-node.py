#!/usr/bin/env python3

from common import get_pat, HttpClient

METRY_PAT = get_pat()
client = HttpClient(METRY_PAT)
response = client.get('/api/2.0/trees?parent=null')

if 200 == response.code:
    if 1 == len(response.body_dict['data'])
        root_node = response.body_dict['data'][0]['_id']
        print(root_node)
    else:
        print('Multiple root nodes found. This may cause trouble.')
else:
    print(response.debug_message())
