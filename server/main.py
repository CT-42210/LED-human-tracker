import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret'

# MQTT client setup
client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)


def on_message(client, userdata, msg):
    if msg.topic == "hello_world":
        print(msg.payload)


client.on_message = on_message
client.subscribe("hello_world")


@app.route("/buttons", methods=["GET", "POST"])
def buttons():
    return render_template("buttons.html")


@app.route("/button_press", methods=["POST"])
def button_press():
    if str(request.form["button"]) == "Red":
        print("Redner red")
        return render_template("color.html", color="red")
    elif str(request.form["button"]) == "Green":
        return render_template("color.html", color="green")
    elif str(request.form["button"]) == "Blue":
        return render_template("color.html", color="blue")

    button = request.form["button"]
    return f"Button {button} was pressed"


@app.route("/", methods=["GET", "POST"])
def hey():
    return render_template("home.html")


if __name__ == '__main__':
    client.loop_start()
    app.run(port=8000)
