import os

class Config:
    SECRET_KEY = 'maybe secr3t key'
    DEBUG = True    # default is True
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_DIR = os.path.join(BASEDIR, "citymapinfo")+'/'
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
