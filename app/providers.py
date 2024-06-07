import requests
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from typing import Dict, Any
from django.conf import settings
from django.core.exceptions import ValidationError


GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'

GITHUB_ACCESS_TOKEN_OBTAIN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_USER_INFO_URL = 'https://api.github.com/user'


class Provider:
    def generate_tokens_for_user(self, user):
        serializer = TokenObtainPairSerializer()
        token_data = serializer.get_token(user)
        access_token = token_data.access_token
        refresh_token = token_data
        return access_token, refresh_token


    def get_first_matching_attr(self, obj, *attrs, default=None):
        for attr in attrs:
            if hasattr(obj, attr):
                return getattr(obj, attr)

        return default


class GoogleProvider(Provider):
    def get_access_token(self, *, code: str, redirect_uri: str) -> str:
        data = {
            'code': code,
            'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
            'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code'
        }
        response = requests.post(GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)

        if not response.ok:
            raise ValidationError('Failed to obtain access token from Google.')

        access_token = response.json()['access_token']

        return access_token


    def get_user_info(self, *, access_token:  str) -> Dict[str, Any]:
        response = requests.get(
            GOOGLE_USER_INFO_URL,
            params={'access_token': access_token}
        )                   

        if not response.ok:
            raise ValidationError('Failed to obtain user info from Google.')

        return response.json()


class GithubProvider(Provider):
    def get_access_token(self, *, code: str, redirect_uri: str) -> str:
        data = {
            'code': code,
            'client_id': settings.GITHUB_OAUTH2_CLIENT_ID,
            'client_secret': settings.GITHUB_OAUTH2_CLIENT_SECRET,
            'redirect_uri': redirect_uri,
        }
        headers = {'Accept': 'application/json'}

        response = requests.post(GITHUB_ACCESS_TOKEN_OBTAIN_URL, data=data, headers=headers)

        data = response.json()

        if not response.ok:
            raise ValidationError('Failed to obtain access token from Github.')

        access_token = response.json()['access_token']
        return access_token


    def get_user_info(self, *, access_token:  str) -> Dict[str, Any]:
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.get(
            GITHUB_USER_INFO_URL,
            headers=headers
        )             

        if not response.ok:
            raise ValidationError('Failed to obtain user info from Github.')

        return response.json()
