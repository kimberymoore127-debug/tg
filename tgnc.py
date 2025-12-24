"""
╔══════════════════════════════════════════════════════════════════════╗
║             ⚡ ULTRA HYPER X BOT SCRIPT v8.0 (ULTIMATE) ⚡           ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  [REQUIRED PACKAGES]                                                 ║
║  >>> pip install python-telegram-bot httpx                           ║
║                                                                      ║
║  [SYSTEM REQUIREMENTS]                                               ║
║  • Python 3.9+ (Optimized for Speed)                                 ║
║  • 4GB+ RAM Recommended for Multi-Threading                          ║
║                                                                      ║
║  [HOW TO RUN]                                                        ║
║  1. pip install python-telegram-bot httpx                            ║
║  2. python tgnc.py                                                   ║
║                                                                      ║
║  [HYPER FEATURES]                                                    ║
║  🚀 Asyncio Event Loop Policy Optimized                              ║
║  ⚡ Zero-Latency Dispatcher                                          ║
║  🛡️ Anti-Flood Wait Bypass (Smart Rotation)                          ║
║  🌪️ Multi-Threaded Spam/NC Engine                                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import os
import sys
import time
import logging
import random
import re
import signal
import traceback
from collections import deque
from datetime import datetime, timedelta
from typing import Dict, Set, List, Optional, Tuple

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.constants import ChatType
from telegram.error import RetryAfter, TimedOut, NetworkError, BadRequest, Forbidden

logging.basicConfig(
    format="%(asctime)s - [ULTRA HYPER X] - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("UltraHyperXBot")

OWNER_ID = 7002714522
DEFAULT_AUTHORIZED_USERS = set()
HYPER_MODE = True
MAX_RETRIES = 3
BASE_RETRY_DELAY = 0.5
MAX_TASKS_PER_CHAT = 100
TASK_CLEANUP_INTERVAL = 30
CONNECTION_TIMEOUT = 30

BOT_TOKENS = [8318784008:AAG7as5qNrRKA3O1x8ncG48tWrIWYAQBDsA]

HEART_EMOJIS = ['❤️', '🧡', '💛', '💚', '💙', '💜', '🤎', '🖤', '🤍', '💘', '💝', '💖', '💗', '💓', '💞', '💌', '💕', '💟', '♥️', '❣️', '💔']

UNAUTHORIZED_MESSAGE = "GAGAN PAPA SE BHEEKH MAANG 🤣🎀😻"

NAME_CHANGE_MESSAGES = [
    "GAGAN TERA BAAP  🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI BHEN KA BHOSADA 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI MAA DEV KE LUND PR 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI MAA KA BHOSADA CHUDA 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI CHUDAYI BY DEV PAPA 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} CVR LE RANDI KE BACCHE 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI MAA RANDI 🔥⃤⃟⃝🐦‍🔥 『🚩』",
    "{target} TERI BHEN KAALI CHUT 🔥⃤⃟⃝🐦‍🔥『🚩』",
]

REPLY_MESSAGES = [
    "{target} ---RDI🐣",
    "{target} चुद गया -!",
    "Aʟᴏᴏ Kʜᴀᴋᴇ {target} Kɪ Mᴀ Cʜᴏᴅ Dᴜɴɢᴀ!",
    "{target} Cʜᴜᴅᴀ🦖🪽",
    "{target} Bᴏʟᴇ GAGAN ᴘᴀᴘᴀ पिताश्री Mᴇʀɪ Mᴀ Cʜᴏᴅ Dᴏ",
    "{target} Kɪ Mᴀ Bᴏʟᴇ GAGAN ᴘᴀᴘᴀ Sᴇ Cʜᴜᴅᴜɴɢɪ",
    "{target} Kɪ Bᴇʜɴ Kɪ Cʜᴜᴛ Kᴀʟɪ Kᴀʟɪ",
    "{target} Kɪ Mᴀ Rᴀɴᴅɪ",
    "{target} ɢᴀʀᴇᴇʙ ᴋᴀ ʙᴀᴄʜʜᴀ",
    "{target} ᴄʜᴜᴅ ᴋᴇ ᴘᴀɢᴀʟ ʜᴏɢᴀʏᴀ",
    "{target} ᴋɪ ʙᴇʜɴ ᴄʜᴏᴅᴜ",
    "{target} ʟᴜɴᴅ ᴄʜᴜsᴇɢᴀ sᴀʙᴋᴀ",
    "{target} ᴋɪ ᴍᴀ ᴋᴏ ᴄʜᴏᴅᴇ ᴅᴇᴠ ᴘᴀᴘᴀ",
    "{target} ᴋɪ ᴍᴀ ᴅᴇᴠ ᴘᴀᴘᴀ ꜱᴇ ᴄʜᴜᴅᴇ",
    "{target} ᴅᴇᴠ ᴘᴀᴘᴀ ꜱᴇ ᴄʜᴜᴅᴀ",
    "{target} CUDKE MARGYA",
    "{target} ɴᴇ GAGAN ᴘᴀᴘᴀ ᴋᴏ ʙᴀᴀᴩ ʙɴᴀ ʟɪyᴀ",
    "{target} ʙᴏʟᴇ GAGAN ᴘᴀᴘᴀ ᴩᴀᴩᴀ",
    "{target} ᴋɪ ᴀᴍᴍᴀ ᴄʜᴜᴅɪ",
    "{target} ᴋᴜᴛᴛᴇ ɢᴜʟᴀᴍɪ ᴋʀ 😋",
]

SPAM_MESSAGES = [
    "✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི",
    "➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐 🤣　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐 🤣　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐 🤣　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐 🤣　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷",
  "➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐👅　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐👅　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐👅　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐👅　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷",
"➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐👅　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐👅　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐👅　➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷➶　　　　　　　➶　　　　　　➶　　　　　➶　　　　　　　　　➤　➷　　　　　　　　➷　　　　 　　　➷　　　　　　➷　　　　　　　　　　　　　　➷{target} 𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 \ 𝘽𝘼𝙃𝘼𝙉 𝘿𝙊𝙉𝙊 𝙆𝙊 𝙍𝘼𝙉𝘿𝙄 𝙆𝙊 𝘾𝙃𝙊𝘿𝙐👅　➶",
"{target} 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵___",
  "{target} 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵__{target}   𝐓𝐄𝐑𝐈 𝐌𝐀𝐀_𝐁𝐀𝐇𝐀𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐁𝐈𝐍𝐀 𝐂𝐎𝐍𝐃𝐎𝐌 𝐊𝐄 😝 𝐇𝐀𝐇𝐀𝐇𝐀 ׂׂૢ🩵___//"
]


def extract_retry_after(error_str):
    match = re.search(r'retry after (\d+)', error_str.lower())
    if match:
        return int(match.group(1))
    return None


async def exponential_backoff_sleep(attempt: int, base_delay: float = BASE_RETRY_DELAY) -> float:
    """Calculate exponential backoff delay with jitter."""
    delay = base_delay * (2 ** min(attempt, 5))
    jitter = random.uniform(0, delay * 0.1)
    total_delay = delay + jitter
    await asyncio.sleep(total_delay)
    return total_delay


async def retry_with_backoff(coro, max_attempts: int = MAX_RETRIES) -> bool:
    """Retry a coroutine with exponential backoff."""
    for attempt in range(max_attempts):
        try:
            await coro
            return True
        except asyncio.CancelledError:
            raise
        except RetryAfter as e:
            wait = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
            logger.warning(f"Rate limited. Waiting {wait}s before retry...")
            await asyncio.sleep(wait + 0.1)
        except (TimedOut, NetworkError) as e:
            if attempt < max_attempts - 1:
                delay = await exponential_backoff_sleep(attempt)
                logger.debug(f"Transient error (attempt {attempt+1}): {type(e).__name__}. Waiting {delay:.2f}s...")
            else:
                logger.error(f"Failed after {max_attempts} attempts: {e}")
                return False
        except Exception as e:
            logger.error(f"Unexpected error: {type(e).__name__}: {e}")
            return False
    return False


ALL_BOT_INSTANCES: Dict[int, 'HyperBotInstance'] = {}
GLOBAL_STOP_EVENT = asyncio.Event()
COMMAND_LOCKS: Dict[int, asyncio.Lock] = {}


def get_command_lock(chat_id: int) -> asyncio.Lock:
    if chat_id not in COMMAND_LOCKS:
        COMMAND_LOCKS[chat_id] = asyncio.Lock()
    return COMMAND_LOCKS[chat_id]


class HyperBotInstance:
    def __init__(self, bot_number, owner_id):
        self.bot_number = bot_number
        self.owner_id = owner_id
        self.authorized_users = set(DEFAULT_AUTHORIZED_USERS)
        self.active_spam_tasks: Dict[int, List[asyncio.Task]] = {}
        self.active_name_change_tasks: Dict[int, List[asyncio.Task]] = {}
        self.active_custom_nc_tasks: Dict[int, List[asyncio.Task]] = {}
        self.active_reply_tasks: Dict[int, asyncio.Task] = {}
        self.active_reply_targets: Dict[int, str] = {}
        self.pending_replies: Dict[int, List[int]] = {}
        self.chat_delays: Dict[int, float] = {}
        self.chat_threads: Dict[int, int] = {}
        self.locks: Dict[int, asyncio.Lock] = {}
        self.stats = {"sent": 0, "errors": 0, "start_time": time.time(), "retries": 0, "rate_limits": 0}
        self.is_running = True
        self.last_cleanup = time.time()
        ALL_BOT_INSTANCES[bot_number] = self
        logger.info(f"Bot {bot_number} initialized successfully")

    def get_lock(self, chat_id):
        if chat_id not in self.locks:
            self.locks[chat_id] = asyncio.Lock()
        return self.locks[chat_id]

    def is_owner(self, user_id):
        return user_id == self.owner_id

    def is_authorized(self, user_id):
        return user_id == self.owner_id or user_id in self.authorized_users

    async def check_owner(self, update):
        user_id = update.effective_user.id
        if not self.is_authorized(user_id):
            try:
                await update.message.reply_text(UNAUTHORIZED_MESSAGE)
            except Exception:
                pass
            return False
        return True

    async def check_main_owner(self, update):
        user_id = update.effective_user.id
        if not self.is_owner(user_id):
            try:
                await update.message.reply_text("⛔ Only the main owner can use this command!")
            except Exception:
                pass
            return False
        return True

    async def cleanup_dead_tasks(self):
        """Remove completed or cancelled tasks from tracking."""
        current_time = time.time()
        if current_time - self.last_cleanup < TASK_CLEANUP_INTERVAL:
            return
        self.last_cleanup = current_time
        
        for chat_id in list(self.active_spam_tasks.keys()):
            self.active_spam_tasks[chat_id] = [t for t in self.active_spam_tasks[chat_id] if not t.done()]
            if not self.active_spam_tasks[chat_id]:
                del self.active_spam_tasks[chat_id]
        
        for chat_id in list(self.active_name_change_tasks.keys()):
            self.active_name_change_tasks[chat_id] = [t for t in self.active_name_change_tasks[chat_id] if not t.done()]
            if not self.active_name_change_tasks[chat_id]:
                del self.active_name_change_tasks[chat_id]
        
        for chat_id in list(self.active_custom_nc_tasks.keys()):
            self.active_custom_nc_tasks[chat_id] = [t for t in self.active_custom_nc_tasks[chat_id] if not t.done()]
            if not self.active_custom_nc_tasks[chat_id]:
                del self.active_custom_nc_tasks[chat_id]

    async def safe_cancel_tasks(self, tasks: List[asyncio.Task]):
        for task in tasks:
            if not task.done():
                task.cancel()
        for task in tasks:
            try:
                await asyncio.wait_for(asyncio.shield(task), timeout=2.0)
            except (asyncio.CancelledError, asyncio.TimeoutError, Exception):
                pass

    async def stop_all_tasks_globally(self):
        all_tasks = []
        
        for chat_id, tasks in list(self.active_spam_tasks.items()):
            all_tasks.extend(tasks)
            del self.active_spam_tasks[chat_id]
            
        for chat_id, tasks in list(self.active_name_change_tasks.items()):
            all_tasks.extend(tasks)
            del self.active_name_change_tasks[chat_id]
            
        for chat_id, tasks in list(self.active_custom_nc_tasks.items()):
            all_tasks.extend(tasks)
            del self.active_custom_nc_tasks[chat_id]
            
        for chat_id, task in list(self.active_reply_tasks.items()):
            all_tasks.append(task)
            del self.active_reply_tasks[chat_id]
            
        self.active_reply_targets.clear()
        self.pending_replies.clear()
        
        await self.safe_cancel_tasks(all_tasks)
        return len(all_tasks)

    async def name_change_loop(self, chat_id, base_name, context, worker_id=1):
        msg_index = 0
        num_messages = len(NAME_CHANGE_MESSAGES)
        success_count = 0
        print(f"[Bot {self.bot_number}] NC Worker #{worker_id} STARTED for chat {chat_id}")
        while True:
            try:
                while self.is_running and not GLOBAL_STOP_EVENT.is_set():
                    delay = self.chat_delays.get(chat_id, 0)
                    try:
                        current_msg = NAME_CHANGE_MESSAGES[msg_index % num_messages]
                        display_name = current_msg.format(target=base_name)
                        await context.bot.set_chat_title(chat_id=chat_id, title=display_name)
                        msg_index += 1
                        success_count += 1
                        self.stats["sent"] += 1
                        if delay > 0:
                            await asyncio.sleep(delay)
                    except asyncio.CancelledError:
                        raise
                    except RetryAfter as e:
                        wait_time = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
                        await asyncio.sleep(wait_time + 0.05)
                    except (TimedOut, NetworkError):
                        pass
                    except (BadRequest, Forbidden):
                        await asyncio.sleep(0.1)
                        msg_index += 1
                    except Exception:
                        self.stats["errors"] += 1
                        msg_index += 1
                break
            except asyncio.CancelledError:
                print(f"[Bot {self.bot_number}] NC Worker #{worker_id} stopped after {success_count} changes")
                break
            except Exception:
                await asyncio.sleep(0.1)

    async def custom_name_change_loop(self, chat_id, custom_name, context, worker_id=1):
        success_count = 0
        print(f"[Bot {self.bot_number}] Custom NC Worker #{worker_id} STARTED for chat {chat_id}")
        while True:
            try:
                while self.is_running and not GLOBAL_STOP_EVENT.is_set():
                    delay = self.chat_delays.get(chat_id, 0)
                    try:
                        heart = random.choice(HEART_EMOJIS)
                        display_name = f"{custom_name} {heart}"
                        await context.bot.set_chat_title(chat_id=chat_id, title=display_name)
                        success_count += 1
                        self.stats["sent"] += 1
                        if delay > 0:
                            await asyncio.sleep(delay)
                    except asyncio.CancelledError:
                        raise
                    except RetryAfter as e:
                        wait_time = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
                        await asyncio.sleep(wait_time + 0.05)
                    except (TimedOut, NetworkError):
                        pass
                    except (BadRequest, Forbidden):
                        await asyncio.sleep(0.1)
                    except Exception:
                        self.stats["errors"] += 1
                break
            except asyncio.CancelledError:
                print(f"[Bot {self.bot_number}] Custom NC Worker #{worker_id} stopped after {success_count} changes")
                break
            except Exception:
                await asyncio.sleep(0.1)

    async def spam_loop(self, chat_id, target_name, context, worker_id):
        success_count = 0
        print(f"[Bot {self.bot_number}] Spam Worker #{worker_id} STARTED for chat {chat_id}")
        while True:
            try:
                while self.is_running and not GLOBAL_STOP_EVENT.is_set():
                    delay = self.chat_delays.get(chat_id, 0)
                    try:
                        spam_msg = random.choice(SPAM_MESSAGES).format(target=target_name)
                        await context.bot.send_message(chat_id=chat_id, text=spam_msg)
                        success_count += 1
                        self.stats["sent"] += 1
                        if delay > 0:
                            await asyncio.sleep(delay)
                    except asyncio.CancelledError:
                        raise
                    except RetryAfter as e:
                        wait_time = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
                        await asyncio.sleep(wait_time + 0.05)
                    except (TimedOut, NetworkError):
                        pass
                    except (BadRequest, Forbidden):
                        await asyncio.sleep(0.1)
                    except Exception:
                        self.stats["errors"] += 1
                break
            except asyncio.CancelledError:
                print(f"[Bot {self.bot_number}] Spam Worker #{worker_id} stopped after {success_count} messages")
                break
            except Exception:
                await asyncio.sleep(0.1)

    async def reply_loop(self, chat_id, target_name, context):
        success_count = 0
        print(f"[Bot {self.bot_number}] Reply LOOP started for chat {chat_id}")
        while True:
            try:
                while self.is_running and not GLOBAL_STOP_EVENT.is_set():
                    delay = self.chat_delays.get(chat_id, 0)
                    if chat_id in self.pending_replies and self.pending_replies[chat_id]:
                        async with self.get_lock(chat_id):
                            messages_to_reply = self.pending_replies[chat_id].copy()
                            self.pending_replies[chat_id] = []

                        for msg_id in messages_to_reply:
                            try:
                                reply_msg = random.choice(REPLY_MESSAGES).format(target=target_name)
                                await context.bot.send_message(
                                    chat_id=chat_id,
                                    text=reply_msg,
                                    reply_to_message_id=msg_id
                                )
                                success_count += 1
                                self.stats["sent"] += 1
                                if delay > 0:
                                    await asyncio.sleep(delay)
                            except asyncio.CancelledError:
                                raise
                            except RetryAfter as e:
                                wait_time = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
                                await asyncio.sleep(wait_time + 0.05)
                            except (TimedOut, NetworkError):
                                pass
                            except (BadRequest, Forbidden):
                                pass
                            except Exception:
                                self.stats["errors"] += 1
                    else:
                        await asyncio.sleep(0.02)
                break
            except asyncio.CancelledError:
                print(f"[Bot {self.bot_number}] Reply LOOP stopped after {success_count} replies")
                break
            except Exception:
                await asyncio.sleep(0.1)

    async def message_collector(self, update, context):
        if not update.message:
            return
        chat_id = update.effective_chat.id
        if chat_id in self.active_reply_targets:
            msg_id = update.message.message_id
            async with self.get_lock(chat_id):
                if chat_id not in self.pending_replies:
                    self.pending_replies[chat_id] = []
                self.pending_replies[chat_id].append(msg_id)

    async def start(self, update, context):
        if not await self.check_owner(update):
            return

        help_text = f"""
𓆩 𝐁𝐎𝐓 {self.bot_number} 𓆪 - ⚡ 𝐔𝐋𝐓𝐑𝐀 𝐇𝐘𝐏𝐄𝐑-𝐗 𝐯𝟖.𝟎 ⚡

━━━━ 🚀 STABILITY & POWER ENHANCED 🚀 ━━━━
✅ Exponential Backoff Retries
✅ Smart Task Cleanup & Memory Management
✅ Better Error Recovery & Logging
✅ Rate Limit Intelligence
✅ Connection Timeout Protection

━━━━ 𝐀𝐓𝐓𝐀𝐂𝐊 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 ━━━━
/target <name> - NC + SPAM together with threads!
/nc <name> - Name change LOOP (with threads)
/ctmnc <custom name> - Custom name + heart emoji LOOP!
/spam <target> - Spam LOOP (with threads)
/reply <target> - Reply to every message LOOP!

━━━━ 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 ━━━━
/delay <seconds> - Set delay (default: 0)
/threads <1-50> - Set threads for NC + SPAM

━━━━ 𝐒𝐓𝐎𝐏 ━━━━
/stopnc - Stop name change loop
/stopctmnc - Stop custom name change loop
/stopspam - Stop spam loop
/stopreply - Stop reply loop
/stopall - Stop ALL loops in this chat
/superstop - STOP ALL BOTS everywhere!

━━━━ 𝐒𝐔𝐃𝐎 (𝐎𝐰𝐧𝐞𝐫 𝐎𝐧𝐥𝐲) ━━━━
/sudo <id1> <id2> ... - Add authorized users
/unsudo <id1> <id2> ... - Remove authorized users
/sudolist - List all authorized users

━━━━ 𝐔𝐓𝐈𝐋𝐈𝐓𝐘 ━━━━
/ping - Show bot latency in ms
/status - Live statistics

𝐓𝐡𝐫𝐞𝐚𝐝𝐬: 1-50 (𝐚𝐩𝐩𝐥𝐢𝐞𝐬 𝐭𝐨 𝐍𝐂 + 𝐒𝐏𝐀𝐌)
𝐀𝐥𝐥 𝐚𝐜𝐭𝐢𝐨𝐧𝐬 𝐫𝐮𝐧 𝐢𝐧 𝐋𝐎𝐎𝐏𝐒 ⚡
𝐎𝐰𝐧𝐞𝐫 𝐎𝐧𝐥𝐲 🔒
"""
        await update.message.reply_text(help_text)

    async def nc_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat = update.effective_chat

        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /nc <name>")
            return

        base_name = " ".join(context.args)
        chat_id = chat.id

        async with get_command_lock(chat_id):
            if chat_id in self.active_name_change_tasks:
                await self.safe_cancel_tasks(self.active_name_change_tasks[chat_id])

            num_threads = self.chat_threads.get(chat_id, 1)
            tasks = []
            for i in range(num_threads):
                task = asyncio.create_task(self.name_change_loop(chat_id, base_name, context, i + 1))
                tasks.append(task)

            self.active_name_change_tasks[chat_id] = tasks

        await update.message.reply_text(f"[Bot {self.bot_number}] Name change LOOP started with {num_threads} threads!")

    async def stop_nc_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id

        async with get_command_lock(chat_id):
            if chat_id in self.active_name_change_tasks:
                await self.safe_cancel_tasks(self.active_name_change_tasks[chat_id])
                del self.active_name_change_tasks[chat_id]
                await update.message.reply_text(f"[Bot {self.bot_number}] Name change LOOP stopped!")
            else:
                await update.message.reply_text(f"[Bot {self.bot_number}] No active name change loop!")

    async def ctmnc_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat = update.effective_chat

        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /ctmnc <custom name>")
            return

        custom_name = " ".join(context.args)
        chat_id = chat.id

        async with get_command_lock(chat_id):
            if chat_id in self.active_custom_nc_tasks:
                await self.safe_cancel_tasks(self.active_custom_nc_tasks[chat_id])

            num_threads = self.chat_threads.get(chat_id, 1)
            tasks = []
            for i in range(num_threads):
                task = asyncio.create_task(self.custom_name_change_loop(chat_id, custom_name, context, i + 1))
                tasks.append(task)

            self.active_custom_nc_tasks[chat_id] = tasks

        await update.message.reply_text(f"[Bot {self.bot_number}] Custom name change LOOP started with {num_threads} threads! Adding heart emojis...")

    async def stop_ctmnc_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id

        async with get_command_lock(chat_id):
            if chat_id in self.active_custom_nc_tasks:
                await self.safe_cancel_tasks(self.active_custom_nc_tasks[chat_id])
                del self.active_custom_nc_tasks[chat_id]
                await update.message.reply_text(f"[Bot {self.bot_number}] Custom name change LOOP stopped!")
            else:
                await update.message.reply_text(f"[Bot {self.bot_number}] No active custom name change loop!")

    async def spam_command(self, update, context):
        print(f"[Bot {self.bot_number}] SPAM COMMAND RECEIVED from user {update.effective_user.id}")
        if not await self.check_owner(update):
            print(f"[Bot {self.bot_number}] User {update.effective_user.id} not authorized for spam")
            return

        chat = update.effective_chat
        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /spam <target_name>")
            return

        target_name = " ".join(context.args)
        chat_id = chat.id

        async with get_command_lock(chat_id):
            if chat_id in self.active_spam_tasks:
                await self.safe_cancel_tasks(self.active_spam_tasks[chat_id])

            num_threads = self.chat_threads.get(chat_id, 1)
            tasks = []
            for i in range(num_threads):
                task = asyncio.create_task(self.spam_loop(chat_id, target_name, context, i + 1))
                tasks.append(task)

            self.active_spam_tasks[chat_id] = tasks

        await update.message.reply_text(f"[Bot {self.bot_number}] Spam LOOP started with {num_threads} threads!")

    async def stop_spam_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id

        async with get_command_lock(chat_id):
            if chat_id in self.active_spam_tasks:
                await self.safe_cancel_tasks(self.active_spam_tasks[chat_id])
                del self.active_spam_tasks[chat_id]
                await update.message.reply_text(f"[Bot {self.bot_number}] Spam LOOP stopped!")
            else:
                await update.message.reply_text(f"[Bot {self.bot_number}] No active spam loop!")

    async def reply_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat = update.effective_chat
        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /reply <target_name>")
            return

        target_name = " ".join(context.args)
        chat_id = chat.id

        async with get_command_lock(chat_id):
            if chat_id in self.active_reply_tasks:
                self.active_reply_tasks[chat_id].cancel()

            self.active_reply_targets[chat_id] = target_name
            self.pending_replies[chat_id] = []
            task = asyncio.create_task(self.reply_loop(chat_id, target_name, context))
            self.active_reply_tasks[chat_id] = task

        await update.message.reply_text(f"[Bot {self.bot_number}] Reply LOOP started for {target_name}!")

    async def stop_reply_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id

        async with get_command_lock(chat_id):
            if chat_id in self.active_reply_tasks:
                self.active_reply_tasks[chat_id].cancel()
                del self.active_reply_tasks[chat_id]
                if chat_id in self.active_reply_targets:
                    del self.active_reply_targets[chat_id]
                if chat_id in self.pending_replies:
                    del self.pending_replies[chat_id]
                await update.message.reply_text(f"[Bot {self.bot_number}] Reply LOOP stopped!")
            else:
                await update.message.reply_text(f"[Bot {self.bot_number}] No active reply loop!")

    async def set_delay_command(self, update, context):
        if not await self.check_owner(update):
            return

        if not context.args or len(context.args) < 1:
            await update.message.reply_text("Usage: /delay <seconds>")
            return

        try:
            delay = float(context.args[0])
            chat_id = update.effective_chat.id
            self.chat_delays[chat_id] = delay
            await update.message.reply_text(f"[Bot {self.bot_number}] Delay set to {delay}s for this chat!")
        except ValueError:
            await update.message.reply_text("Invalid delay value!")

    async def set_threads_command(self, update, context):
        if not await self.check_owner(update):
            return

        if not context.args or len(context.args) < 1:
            await update.message.reply_text("Usage: /threads <count>")
            return

        try:
            threads = int(context.args[0])
            if threads < 1 or threads > 50:
                await update.message.reply_text("Threads must be between 1 and 50!")
                return
            chat_id = update.effective_chat.id
            self.chat_threads[chat_id] = threads
            await update.message.reply_text(f"[Bot {self.bot_number}] Threads set to {threads} for this chat!")
        except ValueError:
            await update.message.reply_text("Invalid thread count!")

    async def add_user_command(self, update, context):
        if not await self.check_main_owner(update):
            return

        if not context.args:
            await update.message.reply_text("Usage: /adduser <user_id>")
            return

        try:
            user_id = int(context.args[0])
            self.authorized_users.add(user_id)
            await update.message.reply_text(f"User {user_id} added to authorized users!")
        except ValueError:
            await update.message.reply_text("Invalid user ID!")

    async def remove_user_command(self, update, context):
        if not await self.check_main_owner(update):
            return

        if not context.args:
            await update.message.reply_text("Usage: /removeuser <user_id>")
            return

        try:
            user_id = int(context.args[0])
            if user_id in self.authorized_users:
                self.authorized_users.discard(user_id)
                await update.message.reply_text(f"User {user_id} removed from authorized users!")
            else:
                await update.message.reply_text(f"User {user_id} is not in the authorized list!")
        except ValueError:
            await update.message.reply_text("Invalid user ID!")

    async def stop_all_command(self, update, context):
        if not await self.check_owner(update):
            return

        count = await self.stop_all_tasks_globally()
        await update.message.reply_text(f"[Bot {self.bot_number}] Stopped {count} active tasks!")

    async def stats_command(self, update, context):
        if not await self.check_owner(update):
            return

        uptime = time.time() - self.stats["start_time"]
        hours, remainder = divmod(int(uptime), 3600)
        minutes, seconds = divmod(remainder, 60)

        stats_text = f"""
📊 Bot {self.bot_number} Stats:
✅ Messages Sent: {self.stats['sent']}
❌ Errors: {self.stats['errors']}
⏱ Uptime: {hours}h {minutes}m {seconds}s
🧵 Active Spam Tasks: {len(self.active_spam_tasks)}
📝 Active NC Tasks: {len(self.active_name_change_tasks)}
💬 Active Reply Tasks: {len(self.active_reply_tasks)}
"""
        await update.message.reply_text(stats_text)


def build_application(token: str, bot_number: int) -> Application:
    bot_instance = HyperBotInstance(bot_number, OWNER_ID)
    
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", bot_instance.start))
    app.add_handler(CommandHandler("help", bot_instance.start))
    app.add_handler(CommandHandler("nc", bot_instance.nc_command))
    app.add_handler(CommandHandler("stopnc", bot_instance.stop_nc_command))
    app.add_handler(CommandHandler("ctmnc", bot_instance.ctmnc_command))
    app.add_handler(CommandHandler("stopctmnc", bot_instance.stop_ctmnc_command))
    app.add_handler(CommandHandler("spam", bot_instance.spam_command))
    app.add_handler(CommandHandler("stopspam", bot_instance.stop_spam_command))
    app.add_handler(CommandHandler("reply", bot_instance.reply_command))
    app.add_handler(CommandHandler("stopreply", bot_instance.stop_reply_command))
    app.add_handler(CommandHandler("delay", bot_instance.set_delay_command))
    app.add_handler(CommandHandler("threads", bot_instance.set_threads_command))
    app.add_handler(CommandHandler("adduser", bot_instance.add_user_command))
    app.add_handler(CommandHandler("removeuser", bot_instance.remove_user_command))
    app.add_handler(CommandHandler("stopall", bot_instance.stop_all_command))
    app.add_handler(CommandHandler("stats", bot_instance.stats_command))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, bot_instance.message_collector))
    
    return app


async def run_bot(token: str, bot_number: int):
    try:
        app = build_application(token, bot_number)
        print(f"[Bot {bot_number}] Starting...")
        await app.initialize()
        await app.start()
        await app.updater.start_polling(drop_pending_updates=True)
        print(f"[Bot {bot_number}] Running!")
        
        while not GLOBAL_STOP_EVENT.is_set():
            await asyncio.sleep(1)
            
        print(f"[Bot {bot_number}] Stopping...")
        await app.updater.stop()
        await app.stop()
        await app.shutdown()
    except Exception as e:
        print(f"[Bot {bot_number}] Error: {e}")


async def main():
    print("=" * 70)
    print("⚡⚡⚡ ULTRA HYPER X BOT v8.0 - STARTING ALL BOTS ⚡⚡⚡")
    print("🚀 ENHANCED STABILITY & POWER MODE 🚀")
    print("=" * 70)
    logger.info("⚡ ULTRA HYPER X v8.0 - ENHANCED WITH EXPONENTIAL BACKOFF & AUTO-CLEANUP")
    
    def signal_handler(sig, frame):
        print("\n🛑 Shutdown signal received...")
        GLOBAL_STOP_EVENT.set()
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    tasks = []
    for i, token in enumerate(BOT_TOKENS, 1):
        task = asyncio.create_task(run_bot(token, i))
        tasks.append(task)
        await asyncio.sleep(0.5)
    
    print(f"\n✅ Started {len(BOT_TOKENS)} bots!")
    print("Press Ctrl+C to stop all bots.\n")
    
    try:
        await asyncio.gather(*tasks, return_exceptions=True)
    except Exception as e:
        print(f"Main error: {e}")
    finally:
        GLOBAL_STOP_EVENT.set()
        for bot in ALL_BOT_INSTANCES.values():
            await bot.stop_all_tasks_globally()
        print("All bots stopped. Goodbye!")


if __name__ == "__main__":
    asyncio.run(main())
