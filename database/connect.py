import os

from redis import Redis

def redis_connect(address=None, port=6379, db=0):
    if address is None:
        address = os.getenv('REDIS_HOST')
    if port is None:
        port = os.getenv('REDIS_PORT')
    
    return Redis(host=address, port=port, db=db)