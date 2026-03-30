# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @ITZZ_ISTKHAR
# ===========================================================

from pyrogram.types import InlineKeyboardButton

import config
from ISTKHAR import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_9"], callback_data="sbot_cb"),  
            InlineKeyboardButton(text=_["S_B_13"], callback_data="abot_cb"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
        ],
    ]
    return buttons

# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 😎
# 
# 🧑‍💻 Developer : t.me/ITZZ_ISTKHAR
# 🔗 Source link : GitHub.com/TEAM-ISTKHAR/ROOHI-V2
# 📢 Telegram channel : t.me/ROOHI_ISTKHAR
# ===========================================================
