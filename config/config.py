import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "1146116"))
API_HASH = getenv("API_HASH", "7ab340d5880dbf53c0940a5bfa37fecc")
BOT_TOKEN = getenv("BOT_TOKEN", "6419873002:AAFi0ulDq86C35mYb6oZxj9fAbIEpul3wWU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "BAB86r0AsmIBouvcT5LAD11J41LLNk5iB4rFxofV3G1UReG2--lzb-QOuVTanEFXkBfX2UMzF-Gn8Faq28mRS1YGRyNJN1oPioacO0HECMyqIT44f1S9TRUkZKCFauJI-MnwrSgQyoD56DVcTLzcQNNfjklCDMLVSA0fVAtuKROylLV8W6RAgIWkkP7WheDLFcHF31o-4UFca8CDz8CCIlVMorhALNPGM8xFmCtVkMoljGQHAuUHTLshI42Jn-c6nusmEZLzEScEtW4opC8YHFRx9-DXQrbVpMqOOtB_VIFfBMyOuw_vjLZHgKoanY7hBRpiCSmfE-hsi13MzNSSip73yPbMYwAAAAGUOxV2AA")
BOT_USERNAME = getenv("BOT_USERNAME", "KAN6_bot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .https://t.me/J_X_Z4").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6291356554").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "
    6291356554").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "1560500120")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "xl444")
GROUP = getenv("GROUP", "xl444")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "
https://t.me/J_X_Z4")
IMG_2 = getenv("IMG_2", "
https://t.me/J_X_Z4")
IMG_5 = getenv("IMG_5", "
https://t.me/J_X_Z4") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "
https://t.me/J_X_Z4")

aiohttpsession = aiohttp.ClientSession()


