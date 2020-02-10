# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
""" Userbot module for other small commands. """

from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, UPSTREAM_REPO_URL
from userbot.events import register


@register(outgoing=True, pattern="^.community$")
async def bot_community(community):
    """ For .community command, just returns OG Paperplane's group link. """
    await community.edit(
        "Join RaphielGang's awesome userbot community: @userbot_support"
        "\nDo note that TG-UBotX is an unoficial fork of their "
        "Paperplane project and it may get limited or no support for bugs.")


@register(outgoing=True, pattern="^.creator$")
async def creator(e):
    await e.edit("Here's my God: [Hitalo](https://t.me/HitaloSama)")


@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    await e.edit(
        "Here's something for you to read:\n"
        "\n[TG-UBotX's README.md file](https://github.com/HitaloKun/TG-UBotX/blob/master/README.md)"
        "\n[Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-07-24)"
        "\n[Setup Guide - Google Drive](https://telegra.ph/How-To-Setup-GDrive-11-02)")


@register(outgoing=True, pattern="^\.random")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit("**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" +
                     itemo[index] + "`")


@register(outgoing=True, pattern="^\.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if " " not in time.pattern_match.group(1):
        await time.reply("Syntax: `.sleep [seconds]`")
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit("`I am sulking and snoozing....`")
        await sleep(2)
        if BOTLOG:
            await time.client.send_message(
                BOTLOG_CHATID,
                "You put the bot to sleep for " + str(counter) + " seconds",
            )
        await sleep(counter)
        await time.edit("`OK, I'm awake now.`")


@register(outgoing=True, pattern="^\.shutdown$")
async def killdabot(event):
    """ For .shutdown command, shut the bot down."""
    await event.edit("`Goodbye *Windows XP shutdown sound*....`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n"
                                        "Bot shut down")
    await bot.disconnect()


@register(outgoing=True, pattern="^\.restart$")
async def killdabot(event):
    await event.edit("`BRB... *PornHub intro*`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n"
                                        "Bot Restarted")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)


# Copyright (c) Gegham Zakaryan | 2019
@register(outgoing=True, pattern="^\.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^\.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        f"Click [here]({UPSTREAM_REPO_URL}) to open my userbot's repository.")


@register(outgoing=True, pattern="^\.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            "`Check the userbot log for the decoded message data !!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`")


CMD_HELP.update({
    "raw":
    ".raw\
\nUsage: Get detailed JSON-like formatted data about replied message.\
\n\n.random <item1> <item2> ... <itemN>\
\nUsage: Get a random item from the list of items.\
\n\n.repeat <no.> <text>\
\nUsage: Repeats the text for a number of times. Don't confuse this with spam tho.\
\n\n.restart\
\nUsage: Restarts the bot !!\
\n\n.readme\
\nUsage: Provide links to setup the userbot and it's modules.\
\n\n.creator\
\nUsage: Know who created this awesome userbot !!\
\n\n.community\
\nUsage: Join the awesome Paperplane userbot community !!\
\n\n.repo\
\nUsage: If you are curious what makes the userbot work, this is what you need.\
\n\n.shutdown\
\nUsage: Sometimes you need to shut down your bot. Sometimes you just hope to\
hear Windows XP shutdown sound... but you don't.\
\n\n.sleep <seconds>\
\nUsage: Userbots get tired too. Let yours snooze for a few seconds."
})