from os import environ

class Config:
    API_ID = environ.get("API_ID", "28249550")
    API_HASH = environ.get("API_HASH", "1a28639a79e913d356bf202e1612fcda")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6344589382:AAFKDjHeFA8eKRhZPv1uoE7jNwGeQHTIm0E")
    BOT_SESSION = environ.get("BOT_SESSION", "bot")
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Merlebot:omNahXZhkYMP4dNf@cluster787.ssmfokm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster787"
    DATABASE_NAME = environ.get("DATABASE_NAME", "Merlebot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1436817644').split()]

class temp(object):
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
