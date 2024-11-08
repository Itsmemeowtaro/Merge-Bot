import os


class Config(object):
    API_HASH = os.environ.get("ef85493cd32eadcb5309b5957d8d1b86")
    BOT_TOKEN = os.environ.get("7961888195:AAFk7fFOKDtybDb3FFJuZbLxttlAM1Wt6eY")
    TELEGRAM_API = os.environ.get("TELEGRAM_API")
    OWNER = os.environ.get("6440021089")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "@Itsme_meowtaro")
    PASSWORD = os.environ.get("meowtaro")
    DATABASE_URL = os.environ.get("mongodb+srv://meow:meow@meow.a6bo1.mongodb.net/?retryWrites=true&w=majority&appName=meow")
    LOGCHANNEL = os.environ.get("-1002134572304")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
