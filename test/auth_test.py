import requests
import pytest
import json

class TestAuth:
    url = ''

    username_json = {'login':'', 'pswd':''}
    wrong_username_json = {'login':'', 'pswd':''}
    email_json = {'login':'', 'pswd':''}
    wrong_email_json = {'login':'', 'pswd':''}

    def test_create_token_with_username_success(self):
        response = requests.get(f'{self.url}/token', json= self.username_json)
        assert response.status_code == 200

    def test_create_with_token_with_email_success(self):
        response = requests.get(f'{self.url}/token', json= self.wrong_username_json)
        assert response.status_code == 200

    def test_create_token_with_username_pswd_error(self):
        response = requests.get(f'{self.url}/token', json= self.wrong_username_json)
        response_json = json.loads(response.json())
        assert response.status_code == 202 and response_json['error'] == 'Invalid user and\\or password'    

    def test_create_token_with_email_pswd_error(self):
        response = requests.get(f'{self.url}/token', json= self.wrong_email_json)
        response_json = json.loads(response.json())
        assert response.status_code == 202 and response_json['error'] == 'Invalid user and\\or password'  

    def test_auth_success(self):
        response = requests.get(f'{self.url}/token', json= self.username_json)
        token = json.loads(response.json())['token']
        response = requests.get(f'{self.url}/auth', headers = {'token' : token})
        assert response.status_code == 200

    def test_auth_no_token(self):
        response = requests.get(f'{self.url}/auth')
        response_json = json.loads(response.json())
        assert response.status_code == 202 and response_json['error'] == 'No token found'
    
    def test_auth_invalid_token(self):
        response = requests.get(f'{self.url}/auth', headers = {'token' : 'NotAToken'})
        assert response.status_code == 500