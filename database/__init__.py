import json

from .connect import redis_connect

DEFAULT_EXPIRE = 86400

# data is a dictionary
def set_link(key, data, expire=DEFAULT_EXPIRE) -> bool: 
    data_str = json.dumps(data)
    r = redis_connect()
    success = r.set(name=key, value=data_str, ex=expire)
    return success

def get_link(key) -> dict:
    r = redis_connect()
    value = r.get(key)
    if value is None:
        return None
    value = value.decode()
    value = json.loads(value)
    return json.loads(value)