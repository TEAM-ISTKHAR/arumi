import os, aiohttp, aiofiles, textwrap
from PIL import Image, ImageDraw, ImageFont

# ✅ cache folder
os.makedirs("cache", exist_ok=True)

# ✅ Unicode safe font loader
def load_font(size):
    try:
        return ImageFont.truetype("ISTKHAR/assets/assets/font3.ttf", size)
    except:
        return ImageFont.load_default()

title_font = load_font(45)
small_font = load_font(30)

# ✅ Unicode safe text
def safe_text(text):
    try:
        text.encode("utf-8")
        return text
    except:
        return text.encode("ascii", "ignore").decode()

# ✅ Safe draw (no crash)
def safe_draw(draw, pos, text, font, fill):
    try:
        draw.text(pos, text, font=font, fill=fill)
    except:
        draw.text(pos, safe_text(text), font=font, fill=fill)

# 🔥 MAIN FUNCTION
async def create_thumb(videoid, user_dp=None, title="Unknown Title", channel="Unknown Channel", duration="0:00"):
    path = f"cache/{videoid}_final.png"

    if os.path.exists(path):
        return path

    thumb_url = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"

    # ✅ download thumbnail
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(thumb_url) as resp:
                if resp.status != 200:
                    return None
                async with aiofiles.open("cache/thumb.jpg", "wb") as f:
                    await f.write(await resp.read())
    except:
        return None

    try:
        base = Image.open("cache/thumb.jpg").resize((1280, 720)).convert("RGBA")

        # ✅ clean dark background
        bg = Image.new("RGBA", (1280, 720), (25, 25, 25))
        draw = ImageDraw.Draw(bg)

        # 🔥 main video thumbnail (left)
        main_thumb = base.resize((700, 400))
        bg.paste(main_thumb, (50, 150))

        # 🔥 USER DP (right circle)
        if user_dp:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(user_dp) as resp:
                        if resp.status == 200:
                            async with aiofiles.open("cache/dp.jpg", "wb") as f:
                                await f.write(await resp.read())

                dp = Image.open("cache/dp.jpg").resize((200, 200)).convert("RGBA")

                mask = Image.new("L", (200, 200), 0)
                mdraw = ImageDraw.Draw(mask)
                mdraw.ellipse((0, 0, 200, 200), fill=255)

                bg.paste(dp, (1000, 180), mask)

            except:
                pass

        # 🔥 TEXT SAFE
        title = safe_text(title)
        channel = safe_text(channel)

        # 🔥 TITLE (right side wrap)
        wrapped = textwrap.wrap(title, width=20)
        y = 420
        for line in wrapped[:2]:
            safe_draw(draw, (900, y), line, title_font, "white")
            y += 50

        # 🔥 CHANNEL
        safe_draw(draw, (900, 520), channel, small_font, (200,200,200))

        # 🔥 DURATION
        safe_draw(draw, (900, 560), f"⏱ {duration}", small_font, "white")

        # 🔥 PROGRESS BAR
        draw.rectangle((900, 600, 1200, 610), fill=(255,255,255,80))
        draw.rectangle((900, 600, 1050, 610), fill=(255,0,0))

        # 🔥 WATERMARK
        safe_draw(draw, (20, 20), "@SukoonxRobot", small_font, "yellow")

        bg.save(path)

        # cleanup
        os.remove("cache/thumb.jpg")
        if os.path.exists("cache/dp.jpg"):
            os.remove("cache/dp.jpg")

        return path

    except Exception as e:
        print("Thumbnail Error:", e)
        return None


# ✅ IMPORTANT (error fix)
async def get_thumb(videoid):
    return await create_thumb(videoid)