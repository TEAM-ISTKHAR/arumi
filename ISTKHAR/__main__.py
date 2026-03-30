# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @ITZZ_ISTKHAR
# ===========================================================

import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ISTKHAR import LOGGER, app, userbot
from ISTKHAR.core.call import ROOHI
from ISTKHAR.misc import sudo
from ISTKHAR.plugins import ALL_MODULES
from ISTKHAR.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗡𝗢𝗧 𝗙𝗜𝗟𝗟𝗘𝗗 🙃, 𝗣𝗟𝗘𝗔𝗦𝗘 𝗙𝗜𝗟𝗟 𝗔 𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗦𝗘𝗦𝗦𝗜𝗢𝗡...🙂")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ISTKHAR.plugins" + all_module)
    LOGGER("ISTKHAR.plugins").info("𝗔𝗟𝗟 𝗣𝗟𝗨𝗚𝗜𝗡𝗦 𝗟𝗢𝗔𝗗𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬....🥳..")
    await userbot.start()
    await ROOHI.start()
    try:
        await ROOHI.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ISTKHAR").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣/𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧... 😒\n\n𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........🤕"
        )
        exit()
    except:
        pass
    await ROOHI.decorators()
    LOGGER("ISTKHAR").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎ 𝗠𝗔𝗗𝗘 𝗕𝗬 𝗣𝗨𝗥𝗩𝗜 𝗕𝗢𝗧𝗦 ☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ISTKHAR").info("𝗦𝗧𝗢𝗣 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧...🥹")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 😎
# 
# 🧑‍💻 Developer : t.me/ITZZ_ISTKHAR
# 🔗 Source link : GitHub.com/TEAM-ISTKHAR/ROOHI-V2
# 📢 Telegram channel : t.me/ROOHI_ISTKHAR
# ===========================================================
