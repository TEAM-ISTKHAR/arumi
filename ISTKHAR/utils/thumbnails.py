import os
import re
import aiohttp
import aiofiles
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch
from config import YOUTUBE_IMG_URL

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

W, H = 1280, 720

# ✅ Safe font loader (Unicode error fix)
def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

title_font = load_font("ISTKHAR/assets/assets/font3.ttf", 60)
small_font = load_font("ISTKHAR/assets/assets/font.ttf", 30)

# ✅ Text trim (overflow fix)
def trim(text, max_len=45):
    return text[:max_len] + "..." if len(text) > max_len else text


# =========================================================
# MAIN FUNCTION (IMPORTANT — import error fix)
# =========================================================
async def get_thumb(videoid: str, player_username: str = "Unknown"):
    path = f"{CACHE_DIR}/{videoid}_final.png"

    if os.path.exists(path):
        return path

    # 🔎 Fetch YouTube data
    try:
        results = await VideosSearch(videoid, limit=1).next()
        data = results["result"][0]

        title = re.sub(r"\W+", " ", data.get("title", "Unknown"))
        duration = data.get("duration", "0:00")
        channel = data.get("channel", {}).get("name", "YouTube")
        thumb_url = data.get("thumbnails", [{}])[0].get("url", YOUTUBE_IMG_URL)

    except Exception:
        return YOUTUBE_IMG_URL

    # 📥 Download thumbnail
    raw = f"{CACHE_DIR}/{videoid}_raw.jpg"

    async with aiohttp.ClientSession() as session:
        async with session.get(thumb_url) as resp:
            if resp.status != 200:
                return YOUTUBE_IMG_URL
            async with aiofiles.open(raw, "wb") as f:
                await f.write(await resp.read())

    # 🖼️ Open image
    base = Image.open(raw).resize((W, H)).convert("RGB")

    # 🔥 BACKGROUND = SAME IMAGE BLUR (FIXED)
    bg = base.filter(ImageFilter.GaussianBlur(35)).convert("RGBA")

    # 🔥 DARK OVERLAY (readability)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 140))
    bg = Image.alpha_composite(bg, overlay)

    draw = ImageDraw.Draw(bg)

    # 🔥 CENTER CARD (clean youtube style)
    card = base.resize((600, 340))
    bg.paste(card, (340, 120))

    # 🔥