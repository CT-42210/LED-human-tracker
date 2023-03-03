import time
import board
import neopixel

pixel_pin = board.D18

num_pixels = 20
offset = int(input("- "))

pixels = neopixel.NeoPixel(pixel_pin, 200, brightness=0.3, auto_write=False)


def color_chase(color, wait):
    for i in range(offset, num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

while True:
    color_chase(CYAN, 0)
    offset = int(input("- "))
