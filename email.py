import os, base64
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

__all__ = ['generate_email']

def generate_email(name, address):
    # addresses are obfuscated as source code is open
    address = base64.b64decode(address)
    img = Image.new('RGB', (800, 40), 'white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 24)
    draw.text((20, 5), address, (0, 0, 0), font=font)
    img.save(os.path.join('docs', name+'.jpg'))
    return name+'.jpg'

