import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from ISTKHAR import app 
from pyrogram.errors import RPCError
import asyncio

# List of photos for logs
photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    for member in message.new_chat_members:
        if member.id == app.id:
            chat = message.chat
            try:
                # Try to get invite link, fallback if not available
                try:
                    link = await app.export_chat_invite_link(chat.id)
                except:
                    link = "No Link"
                
                count = await app.get_chat_members_count(chat.id)
                
                msg = (
                    f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                    f"____________________________________\n\n"
                    f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {chat.title}\n"
                    f"🍂 ᴄʜᴀᴛ ɪᴅ: {chat.id}\n"
                    f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{chat.username if chat.username else 'Private'}\n"
                    f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: {link}\n"
                    f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                    f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention if message.from_user else 'Unknown'}"
                )
                
                # Send Log
                try:
                    markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=link)]]) if link != "No Link" else None
                    await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=markup)
                except Exception:
                    await app.send_message(LOG_GROUP_ID, text=msg)
            except Exception as e:
                print(f"Error in join_watcher: {e}")

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        # Check if the bot itself left or was removed
        bot_id = (await app.get_me()).id
        if bot_id == message.left_chat_member.id:
            remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
            title = message.chat.title
            chat_id = message.chat.id
            
            left = (
                f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n"
                f"𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n"
                f"𝐂ʜᴀᴛ ɪᴅ : {chat_id}\n"
                f"𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n"
                f"𝐁ᴏᴛ : @{(await app.get_me()).username}"
            )
            
            try:
                await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            except Exception:
                await app.send_message(LOG_GROUP_ID, text=left)
    except Exception as e:
        print(f"Error in left_chat_member: {e}")
        
