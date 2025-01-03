import os


class Config(object):
    API_HASH = os.environ.get("42a60d9c657b106370c79bb0a8ac560c")
    BOT_TOKEN = os.environ.get("7820689420:AAFDv2vJ3gsjYhRjz3HpPG8os1-MOBtkAXo")
    TELEGRAM_API = os.environ.get("14050586")
    OWNER = os.environ.get("5446367898")
    OWNER_USERNAME = os.environ.get("『𝚵⃝⃘⃔』⏤͟͟͞͞𝙎𝙝𝙧𝙚𝙚×𝙆𝙧𝙞𝙨𝙝𝙣𝙖⃪➛ㅤㅤㅤᴬᵈᵐⁱⁿ")
    PASSWORD = os.environ.get("@NEW_ANIMES_HINDI_DUB_INDIA")
    DATABASE_URL = os.environ.get("mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1002281888349")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
