from PIL import Image, ImageDraw, ImageFont
import random

def grid_bg(draw, w, h, color, step=16):
    for x in range(0, w, step):
        draw.line([(x,0),(x,h)], fill=color, width=1)
    for y in range(0, h, step):
        draw.line([(0,y),(w,y)], fill=color, width=1)

def make_tile(path, label, glyph_color, bg=(11,14,20), accent=(76,224,210)):
    w=h=256
    img = Image.new("RGB", (w,h), bg)
    d = ImageDraw.Draw(img)
    grid_bg(d, w, h, (20,26,36), step=16)
    # glow ring
    d.ellipse([28,28,w-28,h-28], outline=accent, width=3)
    d.ellipse([48,48,w-48,h-48], outline=glyph_color, width=2)
    # label
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 26)
    except:
        font = ImageFont.load_default()
    bbox = d.textbbox((0,0), label, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    d.text(((w-tw)/2, (h-th)/2 - 6), label, fill=glyph_color, font=font)
    img.save(path)

make_tile("media/logo.png", "GH", (255,79,163), bg=(11,14,20), accent=(76,224,210))
make_tile("media/placeholder.png", "?", (125,139,147), bg=(14,20,32), accent=(90,100,110))
make_tile("media/pong-blitz.png", "PONG", (76,224,210))
make_tile("media/neon-snake.png", "SNK", (255,209,102))
make_tile("media/brick-breaker.png", "BRK", (255,79,163))
print("media done")
