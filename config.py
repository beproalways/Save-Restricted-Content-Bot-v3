# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# Helper function to safely parse integer environment variables
def get_int(key, default=None):
    val = os.getenv(key)
    if not val or val.strip() == "" or val.lower() == "none":
        return default
    try:
        return int(val.strip())
    except ValueError:
        return default

# ════════════════════════════════════════════════════════════════════════════════
# ░ CONFIGURATION SETTINGS
# ════════════════════════════════════════════════════════════════════════════════

# VPS --- FILL COOKIES 🍪 in """ ... """ 
INST_COOKIES = """
# write up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

# ─── BOT / DATABASE CONFIG ──────────────────────────────────────────────────────
API_ID = get_int("API_ID", 36859402)
API_HASH = os.getenv("API_HASH", "6edbd58acf9d0dc413b61aaf0fcf11a8").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
MONGO_DB = os.getenv(
    "MONGO_DB",
    "mongodb+srv://srcbhaisrc:srcbhaisrc@7206@cluster0.thwm8x7.mongodb.net/?appName=Cluster0",
).strip()
DB_NAME = os.getenv("DB_NAME", "srcbhaisrc").strip()

# ─── OWNER / CONTROL SETTINGS ───────────────────────────────────────────────────
OWNER_RAW = os.getenv("OWNER_ID", "7915380485").strip()
OWNER_ID = [int(x) for x in OWNER_RAW.split() if x.isdigit()]
STRING = os.getenv("STRING", None)

# Safe integer casting with fallbacks
LOG_GROUP = get_int("LOG_GROUP", -10044682251662)
FORCE_SUB = get_int("FORCE_SUB", None)

# ─── SECURITY KEYS ──────────────────────────────────────────────────────────────
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq")
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F")

# ─── COOKIES HANDLING ───────────────────────────────────────────────────────────
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)

# ─── USAGE LIMITS ───────────────────────────────────────────────────────────────
FREEMIUM_LIMIT = get_int("FREEMIUM_LIMIT", 0)
PREMIUM_LIMIT = get_int("PREMIUM_LIMIT", 500)

# ─── UI / LINKS ─────────────────────────────────────────────────────────────────
JOIN_LINK = os.getenv("JOIN_LINK", "").strip()
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "").strip()

# ════════════════════════════════════════════════════════════════════════════════
# ░ PREMIUM PLANS CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

P0 = {
    "d": {
        "s": get_int("PLAN_D_S", 1),
        "du": get_int("PLAN_D_DU", 1),
        "u": os.getenv("PLAN_D_U", "days"),
        "l": os.getenv("PLAN_D_L", "Daily"),
    },
    "w": {
        "s": get_int("PLAN_W_S", 3),
        "du": get_int("PLAN_W_DU", 1),
        "u": os.getenv("PLAN_W_U", "weeks"),
        "l": os.getenv("PLAN_W_L", "Weekly"),
    },
    "m": {
        "s": get_int("PLAN_M_S", 5),
        "du": get_int("PLAN_M_DU", 1),
        "u": os.getenv("PLAN_M_U", "month"),
        "l": os.getenv("PLAN_M_L", "Monthly"),
    },
}
