import time
import sys
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.D18
num_pixels = 200

pixels = neopixel.NeoPixel(pixel_pin, 200, brightness=0.3, auto_write=False)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

user_input = input("Enter 'q' to quit: ")

while True:
    while user_input != "q":
        rainbow_cycle(0)
    else:
        color_chase(OFF, 0)
        sys.exit()
