import time
import board
import neopixel

pixel_pin = board.D18


pixels = neopixel.NeoPixel(pixel_pin, 100, brightness=0.3, auto_write=False)


def color_chase(color, offset, num_pixels, reverse):
    if reverse == True:
        for i in reversed(range(offset, num_pixels)):
            pixels[i] = color
            pixels.show()
    else:
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

old_offset = 0

pixel_num = int(input("number of pixels: "))
while True:
    offset = int(input("- "))

    if offset >= old_offset:
        color_chase(OFF, 0, offset, reverse=False)
        color_chase(CYAN, offset, offset + pixel_num, reverse=False)
        color_chase(OFF, pixel_num + offset, 100, reverse=False)
    elif offset <= old_offset:
        if offset >= old_offset:
            color_chase(OFF, pixel_num + offset, 100, reverse=True)
            color_chase(CYAN, offset, offset + pixel_num, reverse=True)
            color_chase(OFF, 0, offset, reverse=True)

    old_offset = offset
