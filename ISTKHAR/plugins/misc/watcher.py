# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @ITZZ_ISTKHAR
# ===========================================================

from pyrogram import filters
from pyrogram.types import Message

from ISTKHAR import app
from ISTKHAR.core.call import ROOHI

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await ROOHI.stop_stream_force(message.chat.id)

# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 😎
# 
# 🧑‍💻 Developer : t.me/ITZZ_ISTKHAR
# 🔗 Source link : GitHub.com/TEAM-ISTKHAR/ROOHI-V2
# 📢 Telegram channel : t.me/ROOHI_ISTKHAR
# ===========================================================
