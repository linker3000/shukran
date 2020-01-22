'''

I2C first steps

For use with 0.96" OLED display (I2C), without reset pin

To use with the Adafruit libraries:

pip3 install adafruit-blinka
pip3 install pillow
pip3 install adafruit-circuitpython-ssd1306
pip3 install pyftdi
pip3 install adafruit-ssd1306
export BLINKA_FT232H=1

Then run the python program...(works in Mu editor)

'''

import adafruit_ssd1306
import board
import busio
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 32     # Change to 64 if needed
BORDER = 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Draw a smaller inner rectangle
draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
               outline=0, fill=0)

# Load default font.
font = ImageFont.load_default()

# Draw Some Text
text = "Linker3000 says HI"
(font_width, font_height) = font.getsize(text)
draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2),
          text, font=font, fill=255)

# Display image
oled.image(image)
oled.show()