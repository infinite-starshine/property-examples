#!/usr/bin/env python3

from common import get_pat, HttpClient

METRY_PAT = get_pat()
client = HttpClient(METRY_PAT)
response = client.get('/api/2.0/accounts/me')

if 200 == response.code:
    is_feature_enabled = 1 == response.body_dict['data']['features']['properties_and_buildings']['value']
    if is_feature_enabled:
        print('Hooray! The properties and buildings features is enabled on your account.')
    else:
        print('The properties and buildings features is NOT enabled on your account.')
else:
    print(response.debug_message())
