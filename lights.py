import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.D18
num_pixels = 200

pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.3)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow_cycle(wait):
    for j in range(255):
        rc_index = j * (256 // num_pixels)
        for i in range(num_pixels):
            pixels[i] = colorwheel(rc_index + i)
            print(i)
        pixels.show()
        time.sleep(wait)


while True:
    rainbow_cycle(0.0)
