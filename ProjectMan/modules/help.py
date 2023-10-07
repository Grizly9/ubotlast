# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/testylawstore & t.me/lawstoreid

from prettytable import PrettyTable
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from ProjectMan import CMD_HELP
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.utility import split_list

@Client.on_message(filters.command("help", CMD_HANDLER) & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        ac = PrettyTable()
        ac.header = False
        ac.title = "LAWSTORE USERBOT"
        ac.align = "l"
        send = client.send_photo
        alive_logo = (
   "https://telegra.ph/file/ae95acb9bc8475d288182.jpg"
)
        for x in split_list(sorted(CMD_HELP.keys()), 2):
            ac.add_row([x[0], x[1] if len(x) >= 2 else None])
law =( f"<b>╔┈「LAW STORE USERBOT」</b>\n"
f"<b>╎❒pemilik:</b> <code>{client.me.mention}<code>\n"
f"<b>╎❒status: PREMIUM</b>\n"
f"<b>╎❒managed by: </b> @lawstoreid\n"
f"<b>╚┈┈┈┈┈┈┈┈┈┈┈┈</b>\n"
f"<b>╔┈「MODULE LIST」</b>\n"
f"<b>╎❒admin</b> \n"
f"<b>╎❒afk</b> \n"
f"<b>╎❒alive</b> \n"
f"<b>╎❒animation</b> \n"
f"<b>╎❒asupan</b> \n"
f"<b>╎❒broadcast</b> \n"
f"<b>╎❒clone</b> \n"
f"<b>╎❒create</b> \n"
f"<b>╎❒fakeaction</b> \n"
f"<b>╎❒globals</b> \n"
f"<b>╎❒google</b> \n"
f"<b>╎❒heroku</b> \n"
f"<b>╎❒info</b> \n"
f"<b>╎❒invite</b> \n"
f"<b>╎❒joinleave</b> \n"
f"<b>╎❒locks</b> \n"
f"<b>╎❒log</b> \n"
f"<b>╎❒memes</b> \n"
f"<b>╎❒memify</b> \n"
f"<b>╎❒misc</b> \n"
f"<b>╎❒parse</b> \n"
f"<b>╎❒paste</b> \n"
f"<b>╎❒ping</b> \n"
f"<b>╎❒pmpermit</b> \n"
f"<b>╎❒profile</b> \n"
f"<b>╎❒purge</b> \n"
f"<b>╎❒quotly</b> \n"
f"<b>╎❒reverse</b> \n"
f"<b>╎❒salam</b> \n"
f"<b>╎❒sosmed</b> \n"
f"<b>╎❒spam</b> \n"
f"<b>╎❒speedtest</b> \n"
f"<b>╎❒start</b> \n"
f"<b>╎❒stats</b> \n"
f"<b>╎❒sticker</b> \n"
f"<b>╎❒system</b> \n"
f"<b>╎❒tag</b> \n"
f"<b>╎❒tagall</b> \n"
f"<b>╎❒telegraph</b> \n"
f"<b>╎❒tiny</b> \n"
f"<b>╎❒translate</b> \n"
f"<b>╎❒vctools</b> \n"
f"<b>╎❒voice</b> \n"
f"<b>╎❒webshot</b> \n"
f"<b>╚┈┈┈┈┈┈┈┈┈┈┈┈</b> \n"
)
try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=law,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(man, disable_web_page_preview=True)

        await message.reply(
            f"**Contoh Ketik** `{CMD_HANDLER}help afk` **Untuk Melihat Informasi Module**"
        )

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"──「 **Help For {str(help_arg).upper()}** 」──\n\n"
            for x in commands:
                this_command += f"  •  **Command:** `{CMD_HANDLER}{str(x)}`\n  •  **Function:** `{str(commands[x])}`\n\n"
            this_command += "© @lawstoreid"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **Bukan Nama Modul yang Valid.**",
            )


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
