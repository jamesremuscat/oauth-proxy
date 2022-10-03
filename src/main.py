from fastapi import FastAPI

import os
import requests


CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
OAUTH_TOKEN_URL = os.environ['OAUTH_TOKEN_URL']


app = FastAPI()

session = requests.Session()


@app.get("/token")
def get_token(code, redirect_uri):

    response = session.post(
        OAUTH_TOKEN_URL,
        params={
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': redirect_uri
        }
    )

    return response.json()


@app.get("/refresh")
def get_token(token):

    response = session.post(
        OAUTH_TOKEN_URL,
        params={
            'grant_type': 'refresh_token',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'refresh_token': token
        }
    )

    return response.json()