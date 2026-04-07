# ===========================================================
# 🚀 ROOHI THUMBNAIL ENGINE 🚀
# ===========================================================

import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from py_yt import VideosSearch

from config import YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    return image.resize((maxWidth, maxHeight))


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

        # download thumbnail
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(f"cache/thumb{videoid}.png", "wb") as f:
                        await f.write(await resp.read())

        youtube = Image.open(f"cache/thumb{videoid}.png").convert("RGBA")

        # background blur
        bg = youtube.resize((1280, 720))
        bg = bg.filter(ImageFilter.GaussianBlur(20))
        bg = ImageEnhance.Brightness(bg).enhance(0.4)

        # main card (same style)
        thumb_w, thumb_h = 840, 460
        thumb = youtube.resize((thumb_w, thumb_h))

        mask = Image.new("L", (thumb_w, thumb_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [(0, 0), (thumb_w, thumb_h)], radius=20, fill=255
        )
        thumb.putalpha(mask)

        x = (1280 - thumb_w) // 2
        y = 130

        # glow
        glow = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        ImageDraw.Draw(glow).rounded_rectangle(
            [(x - 20, y - 20), (x + thumb_w + 20, y + thumb_h + 20)],
            radius=30,
            fill="#FFD700",
        )
        glow = glow.filter(ImageFilter.GaussianBlur(30))
        bg.paste(glow, (0, 0), glow)

        # border
        border = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        ImageDraw.Draw(border).rounded_rectangle(
            [(x - 5, y - 5), (x + thumb_w + 5, y + thumb_h + 5)],
            radius=25,
            outline="#FFD700",
            width=5,
        )
        bg.paste(border, (0, 0), border)

        bg.paste(thumb, (x, y), thumb)

        draw = ImageDraw.Draw(bg)

        # fonts
        try:
            font_title = ImageFont.truetype("ISTKHAR/assets/font.ttf", 45)
            font_small = ImageFont.truetype("ISTKHAR/assets/font2.ttf", 30)
        except:
            font_title = ImageFont.truetype("arial.ttf", 45)
            font_small = ImageFont.truetype("arial.ttf", 30)

        # 🔥 TITLE FIX (same look but controlled)
        if len(title) > 45:
            title = title[:45] + "..."

        def center(text, y_pos, font, color):
            w = draw.textlength(text, font=font)
            draw.text(
                ((1280 - w) / 2, y_pos),
                text,
                fill=color,
                font=font,
                stroke_width=2,
                stroke_fill="black",
            )

        # title
        center(title, y + thumb_h + 40, font_title, "white")

        # ✅ PLAYER FIX (MAIN CHANGE)
        stats = f"YouTube : {views} | Time : {duration} | Player : {user_name}"
        center(stats, y + thumb_h + 90, font_small, "#FFD700")

        # dev text (same style)
        draw.text((950, 30), "Dev :- @ITZZ_ISTKHAR", fill="yellow", font=font_small)
        draw.text((30, 680), "@IAMISTKHAR", fill="white", font=font_small)

        file = f"cache/{videoid}.png"
        bg.save(file)

        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass

        return file

    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL


# ===========================================================
# BACKUP
# ===========================================================

async def get_thumb(videoid, user_name="Unknown"):
    return await gen_thumb(videoid, user_name)


async def get_qthumb(vidid):
    try:
        url = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            return result["thumbnails"][0]["url"].split("?")[0]
    except:
        return YOUTUBE_IMG_URL
