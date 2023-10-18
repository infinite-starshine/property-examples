import os
import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError

class Response:
    def __init__(self, code, headers, body_dict):
        self.code = code
        self.headers = headers
        self.body_dict = body_dict
    @classmethod
    def from_success(cls, response):
        return cls(response.status, response.getheaders(), json.loads(response.read()))
    @classmethod
    def from_error(cls, error):
        return cls(error.code, error.headers, json.load(error.fp))
    def pretty_body(self):
        return json.dumps(self.body_dict, indent=4)
    def debug_message(self):
        out = ''
        out += str(self.code) + '\n\n'
        out += str(self.headers) + '\n'
        out += self.pretty_body() + '\n'
        return out

def make_request(method, endpoint, headers, data):
    url = 'https://app.metry.io' + endpoint
    req = Request(url, method=method, data=data, headers=headers)
    try:
        return Response.from_success(urlopen(req))
    except HTTPError as e:
        return Response.from_error(e)

# Convenience helper. I wouldn't recommend to do global access and cutting off
# runtime like it does, but it helps a bunch for these example scripts.
def get_pat():
    pat = os.environ.get('METRY_PAT')
    if None == pat:
        print('Please set environment variable METRY_PAT to contain your private access token.')
        exit(1)
    return pat

class HttpClient:
    def __init__(self, private_access_token):
        self.private_access_token = private_access_token
    def get(self, endpoint):
        headers = {
            'Authorization': 'Bearer ' + self.private_access_token,
        }
        return make_request('GET', endpoint, headers, None)
    def post(self, endpoint, dict_payload):
        headers = {
            'Authorization': 'Bearer ' + self.private_access_token,
            'Content-Type': 'application/json',
        }
        json_payload = json.dumps(dict_payload).encode('utf-8')
        return make_request('POST', endpoint, headers, json_payload)
    def put(self, endpoint, dict_payload):
        headers = {
            'Authorization': 'Bearer ' + self.private_access_token,
            'Content-Type': 'application/json',
        }
        json_payload = json.dumps(dict_payload).encode('utf-8')
        return make_request('PUT', endpoint, headers, json_payload)
    def delete(self, endpoint, dict_payload):
        headers = {
            'Authorization': 'Bearer ' + self.private_access_token,
            'Content-Type': 'application/json',
        }
        json_payload = json.dumps(dict_payload).encode('utf-8')
        return make_request('DELETE', endpoint, headers, json_payload)
