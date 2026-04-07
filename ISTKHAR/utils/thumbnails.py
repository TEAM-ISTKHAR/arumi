# ===========================================================
# 🚀 ROOHI x ISTKHAR THUMBNAIL ENGINE 🚀
# ===========================================================

import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from py_yt import VideosSearch

from config import YOUTUBE_IMG_URL


# ===========================================================
# CLEAN TEXT (REMOVE EMOJI / BUG SYMBOLS)
# ===========================================================

def clean_text(text):
    return re.sub(r'[^\x00-\x7F]+', '', str(text))


# ===========================================================
# MAIN FUNCTION
# ===========================================================

async def gen_thumb(videoid, user_name="Unknown"):
    os.makedirs("cache", exist_ok=True)

    try:
        url = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(url, limit=1)

        for result in (await results.next())["result"]:
            title = clean_text(result.get("title", "Unknown Title"))
            duration = result.get("duration", "Unknown")
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            views = result.get("viewCount", {}).get("short", "Unknown")

        # ================= DOWNLOAD =================
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(f"cache/thumb{videoid}.png", "wb") as f:
                        await f.write(await resp.read())

        youtube = Image.open(f"cache/thumb{videoid}.png").convert("RGBA")

        # ================= BACKGROUND =================
        bg = youtube.resize((1280, 720))
        bg = bg.filter(ImageFilter.GaussianBlur(20))
        bg = ImageEnhance.Brightness(bg).enhance(0.4)

        # ================= MAIN THUMB (COMPACT SIZE) =================
        thumb_w, thumb_h = 780, 420
        thumb = youtube.resize((thumb_w, thumb_h))

        mask = Image.new("L", (thumb_w, thumb_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [(0, 0), (thumb_w, thumb_h)], radius=18, fill=255
        )
        thumb.putalpha(mask)

        x = (1280 - thumb_w) // 2
        y = 110

        # ================= GLOW =================
        glow = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        ImageDraw.Draw(glow).rounded_rectangle(
            [(x - 18, y - 18), (x + thumb_w + 18, y + thumb_h + 18)],
            radius=25,
            fill="#FFD700",
        )
        glow = glow.filter(ImageFilter.GaussianBlur(25))
        bg.paste(glow, (0, 0), glow)

        # ================= BORDER =================
        border = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        ImageDraw.Draw(border).rounded_rectangle(
            [(x - 5, y - 5), (x + thumb_w + 5, y + thumb_h + 5)],
            radius=20,
            outline="#FFD700",
            width=4,
        )
        bg.paste(border, (0, 0), border)

        bg.paste(thumb, (x, y), thumb)

        draw = ImageDraw.Draw(bg)

        # ================= FONTS =================
        try:
            font_title = ImageFont.truetype("ISTKHAR/assets/font.ttf", 40)
            font_small = ImageFont.truetype("ISTKHAR/assets/font2.ttf", 26)
        except:
            font_title = ImageFont.truetype("arial.ttf", 40)
            font_small = ImageFont.truetype("arial.ttf", 26)

        # ================= TITLE FIX =================
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

        # ================= TEXT =================
        center(title, y + thumb_h + 25, font_title, "white")

        safe_name = clean_text(user_name)
        stats = f"YouTube : {views} | Time : {duration} | Player : {safe_name}"
        center(stats, y + thumb_h + 65, font_small, "#FFD700")

        # ================= WATERMARK =================
        draw.text((950, 30), "Dev :- @ITZZ_ISTKHAR", fill="yellow", font=font_small)
        draw.text((30, 680), "@IAMISTKHAR", fill="white", font=font_small)

        # ================= SAVE =================
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
# BACKUP FUNCTIONS
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
