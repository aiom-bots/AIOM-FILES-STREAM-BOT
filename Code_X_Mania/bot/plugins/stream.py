# (c) Code-X-Mania

import asyncio
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.utils.database import Database
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.vars import Var
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyshorteners import Shortener



def get_shortlink(url):
   shortlink = False 
   try:
      shortlink = Shortener().dagd.short(url)
   except Exception as err:
       print(err)
       pass
   return shortlink
@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio) & ~filters.edited, group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ : \n\n Nᴀᴍᴇ : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n  **Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ @ajvadntr Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i>Jᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="HTML"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=m.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ ʙᴏss** @ajvadntr",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = Var.URL + 'watch/' + str(log_msg.message_id)
        shortlink = get_shortlink(stream_link) 
        if shortlink:
            stream_link = shortlink
        online_link = Var.URL + 'download/'+ str(log_msg.message_id) 
        shortlinka = get_shortlink(online_link)
        if shortlinka:
            online_link = shortlinka
        
        file_size = None
        if m.video:
            file_size = f"{humanbytes(m.video.file_size)}"
        elif m.document:
            file_size = f"{humanbytes(m.document.file_size)}"
        elif m.audio:
            file_size = f"{humanbytes(m.audio.file_size)}"

        file_name = None
        if m.video:
            file_name = f"{m.video.file_name}"
        elif m.document:
            file_name = f"{m.document.file_name}"
        elif m.audio:
            file_name = f"{m.audio.file_name}"

        msg_text ="""
Yᴏᴜ'ʀᴇ Lɪɴᴋ Is Rᴇᴀᴅʏ

<b>Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>

<b>Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>

<b>Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>


Nᴏᴛᴇ :  Lɪɴᴋ Wᴏɴ'ᴛ Exᴘɪʀᴇ Uɴᴛɪʟ I Dᴇʟᴇᴛᴇ

"""

        await log_msg.reply_text(text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Dᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True, parse_mode="Markdown", quote=True)
        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML", 
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ", url=f"online_link")
                       ],[
                            InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/AIOM_BOTS"),
                            InlineKeyboardButton("Gʀᴏᴜᴘ", url="https://t.me/AIOM_BOTS_GROUP")
                        ]
                    ]
                ),
                parse_mode="HTML"
            )
         
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode="Markdown")


@StreamBot.on_message(filters.channel & (filters.document | filters.video) & ~filters.edited, group=-1)
async def channel_receive_handler(bot, broadcast):
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        online_link = Var.URL + 'download/' + str(log_msg.message_id) 
        await log_msg.reply_text(
            text=f"**Cʜᴀɴɴᴇʟ Nᴀᴍᴇ:** `{broadcast.chat.title}`\n**Cʜᴀɴɴᴇʟ ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** {stream_link}",
            quote=True,
            parse_mode="Markdown"
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("sᴛʀᴇᴀᴍ ", url=stream_link),
                     InlineKeyboardButton('Dᴏᴡɴʟᴏᴀᴅ', url=online_link)] 
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(w.x)}s from {broadcast.chat.title}\n\n**Cʜᴀɴɴᴇʟ ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`", disable_web_page_preview=True, parse_mode="Markdown")
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Chanell{e}**")
