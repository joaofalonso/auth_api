import requests
import pytest
import json

url = ''

def test_insert_success():
    r = requests.post(f'{url}/user', json= {'name':'', 'email' : '', 'pswd':''})

    assert r.status_code == 201

def test_insert_already_exists():
    r = requests.post(f'{url}/user', json= {'name':'', 'email' : '', 'pswd':''})
    r_json = json.loads(r.json())
    assert r_json['error'] == 'A user with the same name or email already exists'