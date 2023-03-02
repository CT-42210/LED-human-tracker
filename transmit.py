import paho.mqtt.client as mqtt


def publish(topic, content):
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("section1")

    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect("broker.hivemq.com", 1883, 60)

    client.loop_start()

    client.publish(str(topic), str(content))
