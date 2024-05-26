from os import environ 

class Config:
    API_ID = environ.get("API_ID", "23004101")
    API_HASH = environ.get("API_HASH", "a2e157e87728053027cbb156e41a832a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6961331411:AAH3Ms6hH30_BrDjnVSHr2JX-ttG21vX5Gs") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ironman1475767:vijay14757@cluster0.hpz2jjv.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "ironman1475767")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5409975736').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

