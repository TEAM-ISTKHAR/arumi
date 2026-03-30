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
from ISTKHAR.misc import SUDOERS
from pyrogram import filters
from ISTKHAR import app
import asyncio, config
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from ISTKHAR import app
from ISTKHAR.utils.ROOHI_ban import admin_filter
from ISTKHAR.utils.database import get_assistant

links = {}


@app.on_message(
    filters.group
    & filters.command(["userbotjoin", f"userbotjoin@{app.username}"])
    & ~filters.private
)
async def join_group(client, message):
    chat_id = message.chat.id
    userbot = await get_assistant(message.chat.id)
    userbot_id = userbot.id
    done = await message.reply("<b>ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ</b>...")
    await asyncio.sleep(1)
    
    chat_member = await app.get_chat_member(chat_id, app.id)

    
    if (
        message.chat.username
        and not chat_member.status == ChatMemberStatus.ADMINISTRATOR
    ):
        try:
            await userbot.join_chat(message.chat.username)
            await done.edit_text("<b>✅ ᴀssɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ.</b>")
        except Exception as e:
            await done.edit_text("<b>ɪ ɴᴇᴇᴅ ᴀᴅᴍɪɴ ᴘᴏᴡᴇʀ ᴛᴏ ᴜɴʙᴀɴ ɪɴᴠɪᴛᴇ ᴍʏ ᴀssɪsᴛᴀɴᴛ!</b>")

    
    if message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        try:
            await userbot.join_chat(message.chat.username)
            await done.edit_text("<b>✅ ᴀssɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ.</b>")
        except Exception as e:
            await done.edit_text(str(e))

    
    if message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        userbot_member = await app.get_chat_member(chat_id, userbot.id)
        if userbot_member.status in [
            ChatMemberStatus.BANNED,
            ChatMemberStatus.RESTRICTED,
        ]:
            try:
                await app.unban_chat_member(chat_id, userbot.id)
                await done.edit_text("<b>ᴀssɪsᴛᴀɴᴛ ɪs ᴜɴʙᴀɴɴɪɴɢ...</b>")
                await userbot.join_chat(message.chat.username)
                await done.edit_text(
                    "<b>ᴀssɪsᴛᴀɴᴛ ᴡᴀs ʙᴀɴɴᴇᴅ, ʙᴜᴛ ɴᴏᴡ ᴜɴʙᴀɴɴᴇᴅ, ᴀɴᴅ ᴊᴏɪɴᴇᴅ ᴄʜᴀᴛ ✅</b>"
                )
            except Exception as e:
                await done.edit_text(
                    "<b>ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ, ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ʙᴀɴ ᴘᴏᴡᴇʀ ᴀɴᴅ ɪɴᴠɪᴛᴇ ᴜsᴇʀ ᴘᴏᴡᴇʀ ᴏʀ ᴜɴʙᴀɴ ᴀssɪsᴛᴀɴᴛ ᴍᴀɴᴜᴀʟʟʏ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ ʙʏ /userbotjoin</b>"
                )
        return

    
    if (
        not message.chat.username
        and not chat_member.status == ChatMemberStatus.ADMINISTRATOR
    ):
        await done.edit_text("<b>ɪ ɴᴇᴇᴅ ᴀᴅᴍɪɴ ᴘᴏᴡᴇʀ ᴛᴏ ɪɴᴠɪᴛᴇ ᴍʏ ᴀssɪsᴛᴀɴᴛ.</b>")

    
    if (
        not message.chat.username
        and chat_member.status == ChatMemberStatus.ADMINISTRATOR
    ):
        try:
            try:
                userbot_member = await app.get_chat_member(chat_id, userbot.id)
                if userbot_member.status not in [
                    ChatMemberStatus.BANNED,
                    ChatMemberStatus.RESTRICTED,
                ]:
                    await done.edit_text("<b>✅ ᴀssɪsᴛᴀɴᴛ ᴀʟʀᴇᴀᴅʏ ᴊᴏɪɴᴇᴅ.</b>")
                    return
            except Exception as e:
                await done.edit_text("<b>ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ</b>.")
                await done.edit_text("<b>ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ</b>...")
                invite_link = await app.create_chat_invite_link(
                    chat_id, expire_date=None
                )
                await asyncio.sleep(2)
                await userbot.join_chat(invite_link.invite_link)
                await done.edit_text("<b>✅ ᴀssɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.</b>")
        except Exception as e:
            await done.edit_text(
                f"<b>➻ ᴀᴄᴛᴜᴀʟʟʏ ɪ ғᴏᴜɴᴅ ᴛʜᴀᴛ ᴍʏ ᴀssɪsᴛᴀɴᴛ ʜᴀs ɴᴏᴛ ᴊᴏɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴀɴᴅ ɪ ᴀᴍ ɴᴏᴛ ᴀʙʟᴇ ᴛᴏ ɪɴᴠɪᴛᴇ ᴍʏ ᴀssɪsᴛᴀɴᴛ ʙᴇᴄᴀᴜsᴇ [ ɪ ᴅᴏɴᴛ ʜᴀᴠᴇ  ɪɴᴠɪᴛᴇ ᴜsᴇʀ ᴀᴅᴍɪɴ ᴘᴏᴡᴇʀ ] sᴏ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴀᴅᴍɪɴ ᴘᴏᴡᴇʀ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ ʙʏ- /userbotjoin.</b>\n\n<b>➥ ɪᴅ »</b> @{userbot.username}"
            )

    
    if (
        not message.chat.username
        and chat_member.status == ChatMemberStatus.ADMINISTRATOR
    ):
        userbot_member = await app.get_chat_member(chat_id, userbot.id)
        if userbot_member.status in [
            ChatMemberStatus.BANNED,
            ChatMemberStatus.RESTRICTED,
        ]:
            try:
                await app.unban_chat_member(chat_id, userbot.id)
                await done.edit_text(
                    "<b>ᴀssɪsᴛᴀɴᴛ ɪs ᴜɴʙᴀɴɴᴇᴅ</b>\n<b>ᴛʏᴘᴇ ᴀɢᴀɪɴ:- /userbotjoin.</b>"
                )
                invite_link = await app.create_chat_invite_link(
                    chat_id, expire_date=None
                )
                await asyncio.sleep(2)
                await userbot.join_chat(invite_link.invite_link)
                await done.edit_text(
                    "<b>ᴀssɪsᴛᴀɴᴛ ᴡᴀs ʙᴀɴɴᴇᴅ, ɴᴏᴡ ᴜɴʙᴀɴɴᴇᴅ, ᴀɴᴅ ᴊᴏɪɴᴇᴅ ᴄʜᴀᴛ ✅</b>"
                )
            except Exception as e:
                await done.edit_text(
                    f"<b>➻ ᴀᴄᴛᴜᴀʟʟʏ ɪ ғᴏᴜɴᴅ ᴛʜᴀᴛ ᴍʏ ᴀssɪsᴛᴀɴᴛ ɪs ʙᴀɴɴᴇᴅ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴀɴᴅ ɪ ᴀᴍ ɴᴏᴛ ᴀʙʟᴇ ᴛᴏ ᴜɴʙᴀɴ ᴍʏ ᴀssɪsᴛᴀɴᴛ ʙᴇᴄᴀᴜsᴇ [ ɪ ᴅᴏɴᴛ ʜᴀᴠᴇ  ʙᴀɴ ᴘᴏᴡᴇʀ ] sᴏ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ʙᴀɴ ᴘᴏᴡᴇʀ ᴏʀ ᴜɴʙᴀɴ ᴍʏ ᴀssɪsᴛᴀɴᴛ ᴍᴀɴᴜᴀʟʟʏ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ ʙʏ- /userbotjoin.</b>\n\n<b>➥ ɪᴅ »<b/> @{userbot.username}"
                )
        return


@app.on_message(filters.command("userbotleave") & filters.group & admin_filter)
async def leave_one(client, message):
    try:
        userbot = await get_assistant(message.chat.id)
        await userbot.leave_chat(message.chat.id)
        await app.send_message(
            message.chat.id, "<b>✅ ᴜsᴇʀʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴛʜɪs Chat.</b>"
        )
    except Exception as e:
        print(e)


@app.on_message(filters.command(["leaveall", f"leaveall@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 <b>ᴜsᴇʀʙᴏᴛ</b> ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    try:
        userbot = await get_assistant(message.chat.id)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == config.LOGGER_ID:
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"<b>ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...</b>\n\n<b>ʟᴇғᴛ:</b> {left} ᴄʜᴀᴛs.\n<b>ғᴀɪʟᴇᴅ:</b> {failed} ᴄʜᴀᴛs."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"<b>ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...</b>\n\n<b>ʟᴇғᴛ:</b> {left} chats.\n<b>ғᴀɪʟᴇᴅ:</b> {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id,
            f"<b>✅ ʟᴇғᴛ ғʀᴏᴍ:</b> {left} chats.\n<b>❌ ғᴀɪʟᴇᴅ ɪɴ:</b> {failed} chats.",
  )

# ===========================================================
# ©️ 2025-26 All Rights Reserved by ROOHI ISTKHAR (TEAM-ISTKHAR) 😎
# 
# 🧑‍💻 Developer : t.me/ITZZ_ISTKHAR
# 🔗 Source link : GitHub.com/TEAM-ISTKHAR/ROOHI-V2
# 📢 Telegram channel : t.me/ROOHI_ISTKHAR
# ===========================================================
