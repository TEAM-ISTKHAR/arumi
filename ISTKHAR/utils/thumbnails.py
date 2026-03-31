import os, aiohttp, aiofiles, textwrap
from PIL import Image, ImageDraw, ImageFilter, ImageFont

os.makedirs("cache", exist_ok=True)

def load_font(size):
    try:
        return ImageFont.truetype("ISTKHAR/assets/assets/font3.ttf", size)
    except:
        return ImageFont.load_default()

title_font = load_font(45)
small_font = load_font(30)

def draw_center_text(draw, text, y, font, width):
    lines = textwrap.wrap(text, width=30)
    for line in lines[:2]:
        bbox = draw.textbbox((0,0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        draw.text((x, y), line, font=font, fill="white")
        y += 50

async def create_pro_thumb(videoid, title="Unknown Title", duration="0:00", channel="Channel"):
    path = f"cache/{videoid}_yt.png"

    if os.path.exists(path):
        return path

    thumb_url = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"

    async with aiohttp.ClientSession() as session:
        async with session.get(thumb_url) as resp:
            if resp.status != 200:
                return None
            async with aiofiles.open("cache/temp.jpg", "wb") as f:
                await f.write(await resp.read())

    base = Image.open("cache/temp.jpg").resize((1280, 720)).convert("RGBA")

    # 🔥 Blur background
    bg = base.filter(ImageFilter.GaussianBlur(25))

    # 🔥 Dark overlay
    overlay = Image.new("RGBA", bg.size, (0, 0, 0, 150))
    bg = Image.alpha_composite(bg, overlay)

    draw = ImageDraw.Draw(bg)

    # 🔥 Center thumbnail
    center = base.resize((700, 400))
    x = (1280 - 700) // 2
    y = 100
    bg.paste(center, (x, y))

    # 🔥 Title center (bottom)
    draw_center_text(draw, title, 520, title_font, 1280)

    # 🔥 Channel / playlist name
    bbox = draw.textbbox((0,0), channel, font=small_font)
    text_width = bbox[2] - bbox[0]
    draw.text(((1280 - text_width)//2, 600), channel, font=small_font, fill=(200,200,200))

    # 🔥 Progress bar (centered)
    bar_x1 = 240
    bar_x2 = 1040
    draw.rectangle((bar_x1, 650, bar_x2, 660), fill=(255,255,255,80))
    draw.rectangle((bar_x1, 650, bar_x1+500, 660), fill=(255,0,0))

    # 🔥 Duration
    draw.text((bar_x1, 670), "00:00", font=small_font, fill="white")
    draw.text((bar_x2-80, 670), duration, font=small_font, fill="white")

    # 🔥 Watermark
    draw.text((20, 20), "@SukoonxRobot", font=small_font, fill="yellow")

    bg.save(path)
    os.remove("cache/temp.jpg")

    return path


# ✅ IMPORTANT (error fix ke liye)
async def get_thumb(videoid):
    return await create_pro_thumb(videoid)