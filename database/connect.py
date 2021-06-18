import os

from redis import Redis

def redis_connect(host='redis', port=6379, db=0):
    host = os.getenv('REDIS_HOST') or host
    port = os.getenv('REDIS_PORT') or port
    
    return Redis(host=host, port=port, db=db)