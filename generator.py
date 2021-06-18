from database import get_link
import random
import string

CHOICES = string.ascii_letters + string.digits

def rand_string(length=8):
    end = ''
    for _ in range(length):
        end += random.choice(CHOICES)
    return end

def get_unique_str(min_len=8, max_len=16):
    current_len = min_len
    while current_len <= max_len:
        for _ in range(10):
            rand_str = rand_string(current_len)
            item = get_link(rand_str)
            if item is None:
                return rand_str
                
        current_len += 1
    
    return None

    