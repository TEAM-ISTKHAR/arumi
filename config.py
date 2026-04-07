# ===========================================================
#  ██████╗  ██████╗  ██████╗ ██╗  ██╗██╗
#  ██╔══██╗██╔═══██╗██╔═══██╗██║  ██║██║
#  ██████╔╝██║   ██║██║   ██║███████║██║
#  ██╔══██╗██║   ██║██║   ██║██╔══██║██║
#  ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║
#  ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝
#
#        🚀 ROOHI MUSIC CONFIG 🚀
# ===========================================================

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ======================================================
# 🔑 BASIC CONFIG
# ======================================================
API_ID = int(getenv("API_ID", "24168862"))
API_HASH = getenv("API_HASH", "916a9424dd1e58ab7955001ccc0172b3")
BOT_TOKEN = getenv("BOT_TOKEN", None)

OWNER_ID = int(getenv("OWNER_ID", 7473021518))
OWNER_USERNAME = getenv("OWNER_USERNAME", "ITZZ_ISTKHAR")

BOT_USERNAME = getenv("BOT_USERNAME", "MusicBot")
BOT_NAME = getenv("BOT_NAME", "ROOHI MUSIC")
ASSUSERNAME = getenv("ASSUSERNAME")

# ======================================================
# 🗄 DATABASE & LOGGER
# ======================================================
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

try:
    LOGGER_ID = int(getenv("LOGGER_ID", "-1003834337399"))
except:
    LOGGER_ID = 0

# ======================================================
# ⏱ LIMITS
# ======================================================
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ======================================================
# ❌ AUTO LEAVE DISABLED (MAIN FIX)
# ======================================================
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 999999

# ======================================================
# ☁️ HEROKU CONFIG (FIXED)
# ======================================================
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# ======================================================
# 🌐 APIs
# ======================================================
YTPROXY_URL = getenv("YTPROXY_URL", "https://tgapi.xbitcode.com")
YT_API_KEY = getenv("YT_API_KEY", "xbit_zVATHL2zaR9xkUdxIuhx_UeJodl5zkz4")

# ======================================================
# 🔄 UPDATE SYSTEM
# ======================================================
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TEAM-ISTKHAR/ROOHI")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ======================================================
# 📢 SUPPORT
# ======================================================
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/IamIstkhar")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/THUNDERDEVS")

# ======================================================
# 🎧 SPOTIFY
# ======================================================
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# ======================================================
# 🔐 STRING SESSION
# ======================================================
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# ======================================================
# 🖼 IMAGES
# ======================================================
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/x5lytj.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/leaexg.jpg")

PLAYLIST_IMG_URL = "https://files.catbox.moe/b0e4vk.jpg"
STATS_IMG_URL = "https://files.catbox.moe/psya34.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"

# ======================================================
# ⚙️ SYSTEM
# ======================================================
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ======================================================
# ⏳ TIME CONVERTER
# ======================================================
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ======================================================
# 🚨 VALIDATION
# ======================================================
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("Invalid SUPPORT_CHANNEL URL")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("Invalid SUPPORT_CHAT URL")

# ===========================================================
# 🚀 ROOHI MUSIC SYSTEM READY
# ===========================================================
