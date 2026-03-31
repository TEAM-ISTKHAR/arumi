import os
import re
import aiohttp
import aiofiles
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from youtubesearchpython.__future__ import VideosSearch

# 📁 cache folder ensure
if not os.path.exists("cache"):
    os.makedirs("cache")


def clean_title(title):
    title = re.sub(r"\W+", " ", title)
    return " ".join(title.split()[:5]).title()


async def gen_thumb(videoid: str):
    file_path = f"cache/{videoid}.png"

    if os.path.isfile(file_path):
        return file_path

    try:
        # ⚠️ FIX: URL ki jagah videoid use karo (important)
        results = VideosSearch(videoid, limit=1)
        data = (await results.next())["result"][0]

        title = clean_title(data.get("title", "Unknown Title"))
        duration = data.get("duration", "0:00")
        channel = data.get("channel", {}).get("name", "Unknown Channel")
        thumbnail = data["thumbnails"][0]["url"].split("?")[0]

        # 📥 Download thumbnail
        raw_path = f"cache/{videoid}_raw.png"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(raw_path, "wb") as f:
                        await f.write(await resp.read())
                else:
                    return None

        base = Image.open(raw_path).convert("RGB")

        # 🔥 Background (blur)
        bg = base.resize((1280, 720)).filter(ImageFilter.GaussianBlur(25))

        # 🌑 Dark overlay
        overlay = Image.new('RGBA', bg.size, (0, 0, 0, 120))
        bg = Image.alpha_composite(bg.convert('RGBA'), overlay)

        # 🎵 Center cover (rounded)
        cover = base.resize((350, 350))
        mask = Image.new("L", cover.size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.rounded_rectangle((0, 0, 350, 350), radius=40, fill=255)

        bg.paste(cover, (120, 185), mask)

        draw = ImageDraw.Draw(bg)

        # 🔤 Fonts
        try:
            title_font = ImageFont.truetype("ISTKHAR/ROOHI/f.ttf", 45)
            small_font = ImageFont.truetype("ISTKHAR/ROOHI/f.ttf", 28)
        except:
            title_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

        # 📝 Text UI
        draw.text((520, 220), title, font=title_font, fill=(255, 255, 255))
        draw.text((520, 290), channel, font=small_font, fill=(200, 200, 200))
        draw.text((520, 330), f"Duration: {duration}", font=small_font, fill=(180, 180, 180))

        # 🎚 Progress bar
        bar_x = 520
        bar_y = 400
        bar_width = 500

        draw.rectangle((bar_x, bar_y, bar_x + bar_width, bar_y + 6), fill=(120, 120, 120))
        draw.rectangle((bar_x, bar_y, bar_x + int(bar_width * 0.35), bar_y + 6), fill=(255, 255, 255))

        # 🎮 Player buttons
        draw.text((720, 450), "⏮   ⏸   ⏭", font=title_font, fill=(255, 255, 255))

        # 💾 Save
        bg.convert("RGB").save(file_path)

        # 🧹 cleanup
        if os.path.exists(raw_path):
            os.remove(raw_path)

        return file_path

    except Exception as e:
        print("Thumbnail Error:", e)
        return None