import requests
import pytest
import json

url = ''

def test_create_token_with_username_success():
    r = requests.get(f'{url}/token', json= {'login':'', 'pswd':''})
    print(r.content)
    assert r.status_code == 200

def test_create_with_token_with_email_success():
    r = requests.get(f'{url}/token', json= {'login':'', 'pswd':''})
    print(r.content)
    assert r.status_code == 200

def test_create_token_with_username_pswd_error():
    r = requests.get(f'{url}/token', json= {'login':'', 'pswd':''})
    r_json = json.loads(r.json())
    assert r_json['error'] == 'Invalid user and\or password'

def test_create_token_with_email_pswd_error():
    r = requests.get(f'{url}/token', json= {'login':'', 'pswd':''})
    r_json = json.loads(r.json())
    assert r_json['error'] == 'Invalid user and\or password'
