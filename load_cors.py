import json

def load_cors(PATH=None) -> dict:
    if PATH is None:
        PATH = 'cors_config.json'

    data = {}
    
    try: 
        with open(PATH) as f:
            data = json.loads(f.read())
        return data
    except FileNotFoundError:
        pass
    
    return data