import os, aiohttp, aiofiles
from PIL import Image, ImageDraw, ImageFilter, ImageFont

os.makedirs("cache", exist_ok=True)

def load_font(size):
    try:
        return ImageFont.truetype("ISTKHAR/assets/assets/font3.ttf", size)
    except:
        return ImageFont.load_default()

title_font = load_font(50)
small_font = load_font(28)

async def create_pro_thumb(videoid, title="Unknown Title", duration="0:00"):
    thumb_url = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    path = f"cache/{videoid}_pro.png"

    async with aiohttp.ClientSession() as session:
        async with session.get(thumb_url) as resp:
            if resp.status != 200:
                return None
            async with aiofiles.open("cache/temp.jpg", "wb") as f:
                await f.write(await resp.read())

    base = Image.open("cache/temp.jpg").resize((1280, 720)).convert("RGBA")

    # 🔥 Blur background
    bg = base.filter(ImageFilter.GaussianBlur(25))

    draw = ImageDraw.Draw(bg)

    # 🔥 Dark overlay
    overlay = Image.new("RGBA", bg.size, (0, 0, 0, 120))
    bg = Image.alpha_composite(bg, overlay)

    # 🔥 Center thumbnail (sharp)
    center = base.resize((500, 300))
    bg.paste(center, (390, 150))

    # 🔥 Title (2 lines)
    title = title[:50]
    draw.text((100, 500), title, font=title_font, fill="white")

    # 🔥 Progress bar (neon)
    draw.rectangle((100, 600, 1100, 610), fill=(255,255,255,100))
    draw.rectangle((100, 600, 700, 610), fill=(255,0,0))

    # 🔥 Time text
    draw.text((100, 630), "00:00", font=small_font, fill="white")
    draw.text((1050, 630), duration, font=small_font, fill="white")

    # 🔥 Watermark
    draw.text((900, 20), "@SukoonxRobot", font=small_font, fill="yellow")

    bg.save(path)
    os.remove("cache/temp.jpg")

    return path