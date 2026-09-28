# This basic example shows how to draw shapes and text on Inky Impression using PIL.
# Libby lightly modified version of https://github.com/pimoroni/inky/blob/main/examples/spectra6/hello_world.py

from font_fredoka_one import FredokaOne
from PIL import Image, ImageDraw, ImageFont

from inky.auto import auto

import sys

text = sys.argv[1]

inky_display = auto(ask_user=True, verbose=True)

# Create new PIL image with a white background
image = Image.new("P", (inky_display.width, inky_display.height), inky_display.WHITE)
draw = ImageDraw.Draw(image)

font = ImageFont.truetype(FredokaOne, 72)

# draw some shapes
draw.rectangle((50, 50, 200, 200), fill=inky_display.YELLOW)  # Rectangle
draw.ellipse((150, 150, 300, 300), fill=inky_display.RED)  # Circle (ellipse)
draw.line((0, 0, 400, 400), fill=inky_display.BLUE, width=10)  # Diagonal line

# draw some text
draw.text((0, 0), text, inky_display.BLACK, font)

inky_display.set_image(image)
inky_display.show()

