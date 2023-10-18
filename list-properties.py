#!/usr/bin/env python3

from common import get_pat, HttpClient

METRY_PAT = get_pat()
client = HttpClient(METRY_PAT)
response = client.get('/api/2.0/trees?type=property')

if 200 == response.code:
    for item in response.body_dict['data']:
        node_id = item['_id']

        designation = '(no property designation)'
        if 'property_designation' in item['property']:
            designation = item['property']['property_designation']

        print('%s\t%s' % (node_id, designation))
else:
    print(response.debug_message())
