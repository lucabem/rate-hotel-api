import os

def get_environ(key, default):
    if os.environ.get(key) is None or os.environ.get(key) == '':
        return default
    else:
        return os.environ.get(key)
    
LANDING_PATH   = get_environ('LANDING_PATH', 'data/landing')
LANDING_FORMAT = get_environ('LANDING_FORMAT', 'csv')
THREADS_NUMBER = get_environ('THREADS_NUMBER', 5)