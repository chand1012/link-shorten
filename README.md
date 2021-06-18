# Python Temporary URL Shortener

- All links last 24 hours.
    - The ability to change that length of time will be coming in the near future.
- Can be hosted as open API or an API with a single key.
- Can change the base URL redirect. Currently no support for displaying a web page.
- Uses Redis for high speed links.
- Will eventually support custom links

# To run

Requires [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/engine/reference/commandline/compose/).

 1) (Optional) Copy [`example.env`](/example.env) to `.env`. Change the variables as you see fit. If you don't require a base redirect nor an API key, you can skip this step.
 2) Run `docker-compose up --build -d`
 3) Use it.

# Usage

```
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> test_data = {'link': 'https://www.riverways.app/'}
>>> resp = requests.post('http://127.0.0.1:5000/new', json=test_data)
>>> resp.json()
{'link': 'https://www.riverways.app/', 'expire': 86400, 'resetExpireOnClick': False, 'id': '2XVWK8ZI'}
```

If the environment variable `APIKEY` is specified.

```
>>> header = {'X-Api-Key': 'Your-api-key-here'}
>>> resp = requests.post('http://127.0.0.1:5000/new', json=test_data, headers=header)
>>> resp.json()
{'link': 'https://www.riverways.app/', 'expire': 86400, 'resetExpireOnClick': False, 'id': 'loD4MbMc'}
```