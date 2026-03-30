# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @ITZZ_ISTKHAR
# ===========================================================

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ISTKHAR import app

@app.on_message(filters.command("privacy"))
async def privacy_command(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/0jpf7u.jpg",
        caption="**➻ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʀᴏᴏʜɪ ʙᴏᴛꜱ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ.**\n\n**⊚ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛʜᴇɴ ꜱᴇᴇ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ 🔏**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("˹ ᴘʀɪᴠᴀᴄʏ ˼", url="https://telegra.ph/Privacy-Policy--ROOHI-ISTKHAR-by-ALPHA-BABY-08-06")]
            ]
        )
    )

# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 😎
# 
# 🧑‍💻 Developer : t.me/ITZZ_ISTKHAR
# 🔗 Source link : GitHub.com/TEAM-ISTKHAR/ROOHI-V2
# 📢 Telegram channel : t.me/ROOHI_ISTKHAR
# ===========================================================
