import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe("bruh")
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    print("Received message: " + message.payload.decode())


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)

client.loop_forever()
