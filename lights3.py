import time
import board
import neopixel

pixel_pin = board.D18

pixels = neopixel.NeoPixel(pixel_pin, 200, brightness=0.3, auto_write=False)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

def neo_sweep(np, color, width):
    bkgnd = []
    num_pixels = len(np)
    for i in range(num_pixels + width, 100):
        erase = i - width
        if erase >= 0:
            np[erase] = bkgnd.pop()

        if i < num_pixels:
            bkgnd.insert(0, np[i])
            np[i] = color

        np.show()

neo_sweep(pixels, RED, 10)
