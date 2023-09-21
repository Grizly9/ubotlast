# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/testylawstore & t.me/lawstoreid

import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from ProjectMan import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from ProjectMan.helpers.misc import create_botlog, heroku
from ProjectMan.modules import ALL_MODULES

MSG_ON = """
🔥 **LawStore-UserBotBerhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"ProjectMan.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("lawstoreid")
            await bot.join_chat("testylawstore")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("ProjectMan").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("ProjectMan").info(f"LawStore-UserBotv{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ProjectMan").info("Starting PyroMan-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())
