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

        # background
        bg = youtube.resize((1280, 720))
        bg = bg.filter(ImageFilter.GaussianBlur(20))
        bg = ImageEnhance.Brightness(bg).enhance(0.4)

        # main card
        thumb = youtube.resize((800, 420))

        mask = Image.new("L", (800, 420), 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [(0, 0), (800, 420)], radius=25, fill=255
        )
        thumb.putalpha(mask)

        x = (1280 - 800) // 2
        y = 130

        bg.paste(thumb, (x, y), thumb)

        draw = ImageDraw.Draw(bg)

        # fonts
        try:
            font_title = ImageFont.truetype("arial.ttf", 38)
            font_small = ImageFont.truetype("arial.ttf", 28)
            font_big = ImageFont.truetype("arial.ttf", 60)
        except:
            font_title = font_small = font_big = ImageFont.load_default()

        # title fix
        if len(title) > 35:
            title = title[:35] + "..."

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
        center(title, y + 440, font_title, "white")

        # stats
        stats = f"YouTube : {views} | Time : {duration} | Player : {user_name}"
        center(stats, y + 480, font_small, "yellow")

        # top text
        center("# ISTKHAR", 20, font_big, "yellow")

        # bottom text
        center("ROOHI", 650, font_big, "white")

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
