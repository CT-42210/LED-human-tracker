import paho.mqtt.client as mqtt

client = mqtt.Client()

def mqtt_send(text):
    # MQTT client setup
    client.connect("broker.hivemq.com", 1883, 60)
    client.publish("hello_world", text)

mqtt_send("bruh why wont this work")