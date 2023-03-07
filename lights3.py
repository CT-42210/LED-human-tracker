import board
import neopixel

pixel_pin = board.D18

pixels = neopixel.NeoPixel(pixel_pin, 100, brightness=0.3, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)


def neo_sweep(np, start, stop, color, width, bkgnd):
    try:
        if start < stop:
            for i in range(start, stop):
                erase = i - width
                if erase >= 0:
                    np[erase] = bkgnd.pop()

                if i < stop:
                    bkgnd.insert(0, np[i])
                    np[i] = color

                np.show()

        elif start > stop:
            if start < stop:
                for i in reversed(range(stop, start)):
                    erase = i + width
                    if erase < len(np):
                        np[erase] = bkgnd.pop()
                    if i >= start:
                        bkgnd.insert(0, np[i])
                        np[i] = color

                    np.show()

    except IndexError:
        pass


background = []

start_input = int(input("enter start: "))
stop_input = int(input("enter stop: "))
width_input = int(input("enter width: "))

while True:
    neo_sweep(pixels, start_input, stop_input, RED, width_input, background)
