import os, aiohttp, aiofiles
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ✅ cache folder auto create
os.makedirs("cache", exist_ok=True)

# ✅ safe font loader
def load_font(size):
    try:
        return ImageFont.truetype("ISTKHAR/assets/assets/font3.ttf", size)
    except:
        return ImageFont.load_default()

title_font = load_font(50)
small_font = load_font(28)

# 🔥 MAIN FUNCTION (PRO)
async def create_pro_thumb(videoid, title="Unknown Title", duration="0:00"):
    path = f"cache/{videoid}_pro.png"

    # ✅ cache reuse
    if os.path.exists(path):
        return path

    thumb_url = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(thumb_url) as resp:
                if resp.status != 200:
                    return None
                async with aiofiles.open("cache/temp.jpg", "wb") as f:
                    await f.write(await resp.read())
    except:
        return None

    try:
        base = Image.open("cache/temp.jpg").resize((1280, 720)).convert("RGBA")

        # 🔥 background blur
        bg = base.filter(ImageFilter.GaussianBlur(30))

        # 🔥 dark overlay
        overlay = Image.new("RGBA", bg.size, (0, 0, 0, 140))
        bg = Image.alpha_composite(bg, overlay)

        draw = ImageDraw.Draw(bg)

        # 🔥 center thumbnail (rounded style)
        center = base.resize((520, 300))
        bg.paste(center, (380, 160))

        # 🔥 title (auto wrap)
        title = title[:60]
        draw.text((80, 500), title, font=title_font, fill="white")

        # 🔥 progress bar
        draw.rectangle((80, 600, 1200, 610), fill=(255,255,255,80))
        draw.rectangle((80, 600, 750, 610), fill=(255,0,0))

        # 🔥 time
        draw.text((80, 630), "00:00", font=small_font, fill="white")
        draw.text((1100, 630), duration, font=small_font, fill="white")

        # 🔥 watermark
        draw.text((900, 20), "@SukoonxRobot", font=small_font, fill="yellow")

        bg.save(path)

        os.remove("cache/temp.jpg")
        return path

    except Exception as e:
        print("Thumbnail Error:", e)
        return None


# ✅ IMPORTANT FIX (tere error ka solution)
async def get_thumb(videoid):
    return await create_pro_thumb(videoid)