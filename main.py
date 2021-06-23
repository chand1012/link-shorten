

import os
from typing import Optional

from fastapi import FastAPI
from fastapi.params import Header
from starlette.responses import RedirectResponse, Response
from fastapi.middleware.cors import CORSMiddleware 
from load_cors import load_cors
from database import get_link, set_link
from generator import get_unique_str
from models.new_link import NewLink

API_KEY = os.getenv('APIKEY')
BASE_REDIRECT = os.getenv('BASE_REDIRECT')
CUSTOM_404 = os.getenv('CUSTOM_404')
CORS_CONFIG = os.getenv('CORS_CONFIG')

config = load_cors(CORS_CONFIG)

app = FastAPI()

if config:
    app.add_middleware(CORSMiddleware, **config)

@app.post('/new')
async def new_link(body: NewLink, x_api_key: Optional[str] = Header(None)):

    if not body.link:
        return Response('No link given', 400)

    if API_KEY:
        if x_api_key != API_KEY:
            return Response('Unauthorized', 401)

    body.id = get_unique_str()
    success = set_link(body.id, body.json(), body.expire)

    if not success:
        return Response(None, 500)

    return body

@app.options('/new')
async def options():
    return Response('Success', 200, headers={'Access-Control-Allow-Origin': '*'})

@app.get('/')
async def home():
    
    if BASE_REDIRECT is None:
        return Response("Not found.", 404)
    
    return RedirectResponse(BASE_REDIRECT, 301)

@app.get('/{link_id}')
async def link(link_id):

    link_data = get_link(link_id)

    if link_data is None:
        
        if CUSTOM_404:
            return RedirectResponse(CUSTOM_404, 301)

        return Response('Link not found.', 404)

    url = link_data.get('link')

    if not url:

        if CUSTOM_404:
            return RedirectResponse(CUSTOM_404, 301)

        return Response('Link not found.', 404)

    return RedirectResponse(url, 302)
