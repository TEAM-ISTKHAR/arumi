# ===========================================================
# 🚀 ROOHI THUMBNAIL ENGINE 🚀
# 👑 Dev : @ITZZ_ISTKHAR
# ===========================================================

import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from py_yt import VideosSearch

from config import YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight))


# ===========================================================
# 🔥 MAIN FUNCTION
# ===========================================================

async def gen_thumb(videoid, user_name="Unknown"):
    os.makedirs("cache", exist_ok=True)

    try:
        url = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(url, limit=1)

        for result in (await results.next())["result"]:
            title = result.get("title", "Unknown Title")
            title = re.sub("\W+", " ", title).title()
            duration = result.get("duration", "Unknown")
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            views = result.get("viewCount", {}).get("short", "Unknown")

        # 📥 download thumbnail
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(f"cache/thumb{videoid}.png", "wb") as f:
                        await f.write(await resp.read())

        youtube = Image.open(f"cache/thumb{videoid}.png").convert("RGBA")

        # 🌌 background blur
        bg = changeImageSize(1280, 720, youtube)
        bg = bg.filter(ImageFilter.GaussianBlur(25))
        bg = ImageEnhance.Brightness(bg).enhance(0.35)

        # 🎯 card size (PERFECT)
        thumb_w, thumb_h = 800, 420
        main_thumb = youtube.resize((thumb_w, thumb_h))

        # rounded mask
        mask = Image.new("L", (thumb_w, thumb_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [(0, 0), (thumb_w, thumb_h)], radius=25, fill=255
        )
        main_thumb.putalpha(mask)

        # position
        x = (1280 - thumb_w) // 2
        y = 130

        # ✨ glow
        glow = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        draw_glow = ImageDraw.Draw(glow)
        draw_glow.rounded_rectangle(
            [(x - 15, y - 15), (x + thumb_w + 15, y + thumb_h + 15)],
            radius=30,
            fill="#FFD700",
        )
        glow = glow.filter(ImageFilter.GaussianBlur(30))
        bg.paste(glow, (0, 0), glow)

        # 🟨 border
        border = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        draw_border = ImageDraw.Draw(border)
        draw_border.rounded_rectangle(
            [(x - 5, y - 5), (x + thumb_w + 5, y + thumb_h + 5)],
            radius=28,
            outline="#FFD700",
            width=5,
        )
        bg.paste(border, (0, 0), border)

        # paste main
        bg.paste(main_thumb, (x, y), main_thumb)

        draw = ImageDraw.Draw(bg)

        # 🎨 fonts
        try:
            font_title = ImageFont.truetype("ISTKHAR/assets/font.ttf", 38)
            font_small = ImageFont.truetype("ISTKHAR/assets/font2.ttf", 28)
        except:
            font_title = ImageFont.truetype("arial.ttf", 38)
            font_small = ImageFont.truetype("arial.ttf", 28)

        # 🔥 TITLE CONTROL (NO BIG TEXT)
        if len(title) > 35:
            title = title[:35] + "..."

        def center_text(text, y_pos, font, fill):
            w = draw.textlength(text, font=font)
            draw.text(
                ((1280 - w) / 2, y_pos),
                text,
                fill=fill,
                font=font,
                stroke_width=2,
                stroke_fill="black",
            )

        # 🎵 title
        center_text(title, y + thumb_h + 15, font_title, "white")

        # 👤 dynamic player
        stats = f"YouTube : {views} | Time : {duration} | Player : {user_name}"
        center_text(stats, y + thumb_h + 55, font_small, "#FFD700")

        # 🔥 branding
