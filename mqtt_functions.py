import paho.mqtt.client as mqtt


def receiver(topic):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            client.subscribe(topic)
        else:
            print("Connection failed")

    def on_message(client, userdata, message):
        return ("Received message: " + message.payload.decode())

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("broker.hivemq.com", 1883)

    client.loop_forever()

def publish(topic, content):
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("section1")

    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect("broker.hivemq.com", 1883, 60)

    client.loop_start()

    client.publish(str(topic), str(content))
