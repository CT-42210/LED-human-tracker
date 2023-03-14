import paho.mqtt.client as mqtt
import time
import os
import board
import neopixel
import ast

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

# this is for scyncing pixels to led_strip
LED_multiplication_number = 0.04

LED_LIGHTS = 100
pixels = neopixel.NeoPixel(board.D18, LED_LIGHTS)


# splice_message
#   input = msg.payload | from on_message
#   output = msg.payload in a combined string without b' (someMessage) '
#   purpose --> return a string of mqtt message sent  |  This is later an input do ledHandler


def splice_message(payload):
    ledSectionList = []
    for character in str(payload).replace("\'", "").replace("b", ""):
        # print(character, end="")
        ledSectionList.append(character)
    message = ''.join(ledSectionList)
    return message


# ledHandler
#   input = message (from splice_message()) and current color
#   output = return's new color, however also controls LED lights, and stops script if "stop" is recieved
#   purpose --> control LED lights and change color of strip
def ledHandler(message, color):
    active_leds = []

    if message == "stop":
        client.disconnect()
        client.loop_stop()
        os._exit(101)
    elif isinstance(message, list):
        for cord in message:
            pixel_num = round(cord[0]*LED_multiplication_number)

            active_leds.append(pixel_num)

            pixels[round(cord[0]*LED_multiplication_number)] = color
            pixels[pixel_num+1] = color
            pixels[pixel_num-1] = color
            print(cord[0])
        for led_pixel in range(100):
            if led_pixel not in active_leds:
                pixels[led_pixel] = [0, 0, 0]
            else:
                pass
    else:
        pass


# colorHandler
#   input = message (from spice_message()) and color_start (original color from setup)
#   output = a color that becomes the color variable within mqtt_to_pixels() and is also color of LEDs
#   purpose --> a handler to change the LED strips color
def colorHandler(message, color_start):
    colors = {"red": [255, 0, 0], "green": [0, 0, 255], "blue": [0, 255, 0]}
    if message == "Blue":
        return colors["blue"]
    elif message == "Red":
        return colors["red"]
    elif message == "Green":
        return colors["green"]
    else:
        return color_start


def mqtt_to_pixels(payload, color_start):
    message = ast.literal_eval(payload)
    # color = colorHandler(message, color_start)
    ledHandler(message, color_start)


# RP4_WCAM_HLTRACKERP1 should be topic name
def setup(topic_name):
    # MQTT client setup

    def on_message(client, userdata, msg):
        # the fill shouldn't be necessary anymore
        # pixels.fill((0, 0, 0))
        if msg.topic == topic_name:
            string_list = str(msg.payload).replace("b", "")
            string_list = string_list.replace("'", "")
            print(string_list)
            mqtt_to_pixels(string_list, [0, 255, 0])

    client.on_message = on_message
    client.subscribe(topic_name)
    client.loop_start()
    while True:
        time.sleep(0)


setup("RP4_WCAM_HLTRACKERP1")
# setup("bruh/1")

