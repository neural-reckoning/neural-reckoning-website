# -*- coding: utf-8 -*-
import os, base64
from PIL import Image, ImageFont, ImageDraw, ImageChops

__all__ = ['generate_email']

# from http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def generate_email(name, address, cached):
    basefname = name+'.jpg'
    fname = os.path.join('docs', basefname)
    if basefname in cached and cached[basefname]==address and os.path.exists(fname):
        return basefname
    # addresses are obfuscated as source code is open
    decoded_address = base64.b64decode(address)
    img = Image.new('RGB', (800, 40), 'white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 24)
    draw.text((20, 5), decoded_address, (0, 0, 0), font=font)
    img = trim(img)
    img.save(os.path.join('docs', basefname))
    cached[basefname] = address
    return basefname

