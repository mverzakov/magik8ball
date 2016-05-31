#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def generate_img(temp, description, postfix):
    img = Image.open("answers/empty.png")
    draw = ImageDraw.Draw(img)
    fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
    font = ImageFont.truetype(os.path.join(fonts_path, 'FreeSans.ttf'), 25)
    draw.text((380, 350), temp, (255,255,255), font=font)
    draw.text((360, 400), description, (255, 255, 255), font=font)
    img.save('answers/weather-{}.jpg'.format(postfix))
    return img


if __name__ == '__main__':
    generate_img(str(23), u'Ясно')