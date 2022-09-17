import re
import requests
import pytest

url = ''
def test_insert_success():
    r = requests.post(f'{url}/user', json= {'name':'user_name', 'email' : 'user@email.com', 'pswd':'password'})
    print(r.content)
    assert r.status_code == 200
