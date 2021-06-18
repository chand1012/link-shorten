

import os
from typing import Optional

from fastapi import FastAPI
from fastapi.params import Header
from starlette.responses import RedirectResponse, Response

from database import get_link, set_link
from generator import get_unique_str
from models.new_link import NewLink

app = FastAPI()

@app.post('/new')
async def new_link(body: NewLink, x_api_key: Optional[str] = Header(None)):

    api_key = os.getenv('APIKEY')

    if api_key:
        if x_api_key != api_key:
            return Response('Unauthorized', 401)

    body.id = get_unique_str()
    success = set_link(body.id, body.json(), body.expire)

    if not success:
        return Response(None, 500)

    return body

@app.get('/')
async def home():
    base_redirect = os.getenv('BASE_REDIRECT')

    if base_redirect is None:
        return Response("Not found.", 404)
    
    return RedirectResponse(base_redirect, 301)

@app.get('/{link_id}')
async def link(link_id):

    link_data = get_link(link_id)

    if link_data is None:
        return Response('Link not found.', 404)

    url = link_data.get('link')

    if url is None:
        return Response('Link not found.', 404)

    return RedirectResponse(url, 302)
