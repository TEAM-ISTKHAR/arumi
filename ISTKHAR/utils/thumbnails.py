import os, aiohttp, aiofiles, textwrap
from PIL import Image, ImageDraw, ImageFont

os.makedirs("cache", exist_ok=True)

def load_font(size):
    try:
        return ImageFont.truetype("ISTKHAR/assets/assets/font3.ttf", size)
    except:
        return ImageFont.load_default()

title_font = load_font(45)
small_font = load_font(30)

async def create_thumb(videoid, user_dp=None, title="Unknown", channel="Channel", duration="0:00"):
    path = f"cache/{videoid}_final.png"

    if os.path.exists(path):
        return path

    thumb_url = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"

    # ✅ download video thumbnail
    async with aiohttp.ClientSession() as session:
        async with session.get(thumb_url) as resp:
            if resp.status != 200:
                return None
            async with aiofiles.open("cache/thumb.jpg", "wb") as f:
                await f.write(await resp.read())

    base = Image.open("cache/thumb.jpg").resize((1280, 720)).convert("RGBA")

    # ✅ CLEAN BACKGROUND (no blur)
    bg = Image.new("RGBA", (1280, 720), (20, 20, 20))  # dark clean bg

    draw = ImageDraw.Draw(bg)

    # 🔥 main thumbnail (left side)
    main_thumb = base.resize((700, 400))
    bg.paste(main_thumb, (50, 150))

    # 🔥 USER DP (right side circle)
    if user_dp:
        async with aiohttp.ClientSession() as session:
            async with session.get(user_dp) as resp:
                if resp.status == 200:
                    async with aiofiles.open("cache/dp.jpg", "wb") as f:
                        await f.write(await resp.read())

        dp = Image.open("cache/dp.jpg").resize((200, 200)).convert("RGBA")

        # circle mask
        mask = Image.new("L", (200, 200), 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0, 200, 200), fill=255)

        bg.paste(dp, (1000, 200), mask)

    # 🔥 TITLE (right side)
    wrapped = textwrap.wrap(title, width=20)
    y_text = 420
    for line in wrapped[:2]:
        draw.text((900, y_text), line, font=title_font, fill="white")
        y_text += 50

    # 🔥 CHANNEL
    draw.text((900, 520), channel, font=small_font, fill=(200,200,200))

    # 🔥 DURATION
    draw.text((900, 560), f"⏱ {duration}", font=small_font, fill="white")

    # 🔥 WATERMARK
    draw.text((20, 20), "@SukoonxRobot", font=small_font, fill="yellow")

    bg.save(path)

    os.remove("cache/thumb.jpg")
    if os.path.exists("cache/dp.jpg"):
        os.remove("cache/dp.jpg")

    return path


# ✅ FIX for your bot
async def get_thumb(videoid):
    return await create_thumb(videoid)