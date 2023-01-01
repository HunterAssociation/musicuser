import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>🛠 MENU BANTUAN MUSIC PLAYER

⚡ PERINTAH UNTUK SEMUA ORANG
• {HNDLR}play [judul lagu | link youtube | balas file audio] - untuk memutar lagu
• {HNDLR}vplay [judul video | link youtube | balas file video] - untuk memutar video
• {HNDLR}playlist untuk melihat daftar putar
• {HNDLR}ping - untuk cek status
• {HNDLR}id - untuk melihat id pengguna
• {HNDLR}video - judul video | link yt untuk mencari video
• {HNDLR}song - judul lagu | link yt untuk mencari lagu
• {HNDLR}help - untuk melihat daftar perintah
• {HNDLR}join- untuk join | ke grup 

⚡ PERINTAH UNTUK SEMUA ADMIN
• {HNDLR}resume - untuk melanjutkan pemutaran lagu atau video
• {HNDLR}pause - untuk untuk menjeda pemutaran lagu atau video
• {HNDLR}skip - untuk melewati lagu atau video
• {HNDLR}end - untuk mengakhiri pemutaran</b>
"""
    await m.reply(HELP)
