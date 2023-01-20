import paho.mqtt.client as mqtt

client = mqtt.Client()


# when using the mqtt_setup make sure that the string is a b'' string
def mqtt_setup():
    # MQTT client setup
    client.connect("broker.hivemq.com", 1883, 60)


def mqtt_send(text):
    client.publish("hello_world", text)


# mqtt_setup()
# mqtt_send(b"cheese")


