import urllib.parse
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
đ Hello {},

đ¤ My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.

đ§ Don't know how to do? No worries, just press the help button.

đ¨âđģ My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>."""

HELP_TEXT = """<b>âšī¸ HELP</b>

Here is the list of my commands, please read carefully everything. if anything happened to you then we are not responsible."""

HOWTOUSEME_TEXT = """<b>âšī¸ Help</b> > How To Use Me

<b>đ¤ For an individual:</b>

My name is Hagdmansa Mega Bot, I am a member of Hagdmansa family. I can provide you direct download link of any telegram file/media. If you send me any file/media I will give an external download link, you can use that link to download any file outside telegram. My link is supported in any browser.

âĸ Send me any file/media from Telegram.
âĸ I Will provide an external download link for you.
âĸ All links will be permanent and have the fastest speed.

<b>đĨ For groups/channels:</b>

I also work in public/private groups/channels. If you have multiple files in your group/channel then just add me to your group/channel, I will add an external download link on each file which will be added after I joined the group/channel.

âĸ I must be an admin in your channel/group.
âĸ Don't forget to give all permissions otherwise I will not work.

<b>đ Warning:</b>

âĸ 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this."""

INSTRUCTIONS_TEXT = """<b>âšī¸ Help</b> > Instructions

<b>đ¤ Instructions for an individual:</b>

1. Don't send photos to the bot, send them as a file.
2. Don't send multiple files at a time, send them one by one.

<b>đĨ Instructions for groups/channels:</b>

1. Don't send too many files to your groups/channels.
2. Bot takes time to generate and edit links, keep patience.

<b>đ Warning:</b>

âĸ 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this."""

TUTORIALS_TEXT = """<b>âšī¸ Help</b> > Tutorials

All tutorials related to Bots, Website, Movies and etc, will be updated here. Till then you can visit my movie website <b>www.hagadmansa.com</b> to watch movies. Don't forget to subscribe my updates channel <b>@hagadmansa</b>.

<b>đ Warning:</b>

âĸ 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this."""

ABOUT_TEXT = """<b>đ About</b>

<b>â¯ My Name:</b> Hagadmansa Mega Bot
<b>â¯ Creator:</b> <a href='https://t.me/hagadmansa'>Hagadmansa</a>
<b>â¯ Library:</b> <a href='https://pyrogram.org'>Pyrogram</a>
<b>â¯ Language:</b> <a href='https://Python.org'>Python</a>
<b>â¯ Database:</b> <a href='https://mongodb.com'>MongoDB</a>
<b>â¯ Server:</b> <a href='https://heroku.com'>Heroku</a>
<b>â¯ Channel:</b> <a href='https://t.me/hagadmansa'>Hagadmansa</a>
<b>â¯ Group:</b> <a href='https://t.me/hagadmansachat'>Hagadmansa Support</a>
<b>â¯ Brothers:</b> <a href='https://t.me/hagadmansabot'>Hagadmansa Bot</a>, <a href='https://t.me/hagadmansarobot'>Hagadmansa Robot</a>"""

RATING_TEXT = """<b>đ About</b> > Rating

I have a public channel a private channel and 3 bots, along with this also I have a website. you can rate and write a review on our public channel and bots.

<b>đŖ @hagadmansa</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansa'>here</a>
2. Review this channel <a href='https://t.me/tlgrmcbot?start=hagadmansa-review'>here</a>

<b>đ¤ @hagadmansabot</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansabot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansabot-review'>here</a>

<b>đ¤ @hagadmansarobot</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansarobot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansarobot-review'>here</a>

<b>đ¤ @hagadmansamegabot</b> 

1. Details are <a href='https://t.me/tlgrmcbot?star=hagadmansamegabot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansamegabot-review'>here</a>"""

SOURCE_TEXT = """<b>đ About</b> > Source

<b>âī¸NOTE:</b>

We are not open source yet, if in future we are open our code for everyone then we'll update the source code here."""

DONATE_TEXT = """<b>đ About</b> > Donate

<b>âī¸NOTE:</b>

We are not raising any funds right now, if in future we raise funds then we'll update here."""

START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('đŖ Updates', url='https://t.me/hagadmansa')
            ],[
            InlineKeyboardButton('âšī¸ Help', callback_data='help'),
            InlineKeyboardButton('đ About', callback_data='about')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('â How to use me', callback_data='howtouseme')
            ],[
            InlineKeyboardButton('âī¸ Instructions', callback_data='instructions'),
            InlineKeyboardButton('đš Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('đ Back', callback_data='home'),
            InlineKeyboardButton('đŖ Channel', url='https://t.me/hagadmansa')
        ]]
    )
HOWTOUSEME_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='help'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )
INSTRUCTIONS_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='help'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
   )
TUTORIALS_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='help'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Visit Our Website', url='https://hagadmansa.com')
            ],[
            InlineKeyboardButton('â­ī¸ Rating', callback_data='rating'),
            InlineKeyboardButton('â¤ī¸ Source', callback_data='source'),
            ],[
            InlineKeyboardButton('đ Back', callback_data='home'),
            InlineKeyboardButton('đ¤ Donate', callback_data='donate')
        ]]
    )
RATING_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='about'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )
SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='about'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )
DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='about'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
         )       
    elif update.data == "howtouseme":
        await update.message.edit_text(
            text=HOWTOUSEME_TEXT,
            disable_web_page_preview=True,
            reply_markup=HOWTOUSEME_BUTTONS
        )
    elif update.data == "instructions":
        await update.message.edit_text(
            text=INSTRUCTIONS_TEXT,
            disable_web_page_preview=True,
            reply_markup=INSTRUCTIONS_BUTTONS
        )
    elif update.data == "tutorials":
        await update.message.edit_text(
            text=TUTORIALS_TEXT,
            disable_web_page_preview=True,
            reply_markup=TUTORIALS_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )     
    elif update.data == "rating":
        await update.message.edit_text(
            text=RATING_TEXT,
            disable_web_page_preview=True,
            reply_markup=RATING_BUTTONS
        )    
    elif update.data == "source":
        await update.message.edit_text(
            text=SOURCE_TEXT,
            disable_web_page_preview=True,
            reply_markup=SOURCE_BUTTONS
        )  
    elif update.data == "donate":
        await update.message.edit_text(
            text=DONATE_TEXT,
            disable_web_page_preview=True,
            reply_markup=DONATE_BUTTONS
        )
    else:
        await update.message.delete()

def get_media_file_size(m):
    media = m.video or m.audio or m.document
    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_file_name(m):
    media = m.video or m.document or m.audio
    if media and media.file_name:
        return urllib.parse.quote_plus(media.file_name)
    else:
        return None


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started bot."
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry you are banned to use me, contact support @hagadmansachat.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="đ Join my updates channel to use me.",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("đĄ Join Now", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went wrong contact support @hagadmansachat.",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry you are banned to use me, contact support @hagadmansachat.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="đ You need to join my updates channel to use me. Due to overload only channel subscribers can use me.",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("đĄ Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")],
                         [InlineKeyboardButton("đ Refresh / Try Again", url=f"https://t.me/{(await b.get_me()).username}?start={usr_cmd}")
                        
                        ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went wrong contact support @hagadmansachat.",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))
        file_name = get_media_file_name(get_msg)
        file_size = humanbytes(get_media_file_size(get_msg))

        stream_link = "https://{}/{}/{}".format(Var.FQDN, get_msg.message_id, file_name) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id,
                                     file_name)

        msg_text ="""
<b><u>Here is your link.</u></b>\n
<b>đ File Name:</b> <code><i>{}</i></code>\n
<b>đĻ File Size:</b> <i>{}</i>\n
<b>đĨ Download:</b> <i>{}</i>\n
<b>đ¸ Note:</b> This is a permanent link.\n
<b>đ Warning:</b> 18+ Content will permanently ban you."""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("đĨ Download Now", url=stream_link)]])
        )



@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started bot."
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry you are banned to use me, contact support @hagadmansachat.",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="đ You need to join my updates channel to use me. Due to overload only channel subscribers can use me.",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("đĄ Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went wrong contact support @hagadmansachat.",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )

