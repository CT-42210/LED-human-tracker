import time
import board
import neopixel

pixel_pin = board.D18


pixels = neopixel.NeoPixel(pixel_pin, 200, brightness=0.3, auto_write=False)


def color_chase(color, offset, num_pixels):
    for i in range(offset, num_pixels):
        pixels[i] = color
        pixels.show()


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

pixel_num = int(input("number of pixels: "))
while True:
    offset = int(input("- "))
    color_chase(OFF, 0, offset)
    color_chase(CYAN, offset, pixel_num)
    color_chase(OFF, pixel_num + offset, 200)
