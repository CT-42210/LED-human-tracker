import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
import sys

def mqtt_setup():
    # MQTT client setup
    client = mqtt.Client()
    client.connect("broker.hivemq.com", 1883, 60)

    def on_message(client, userdata, msg):
        if msg.topic == "hello_world":
            print(msg.payload)

    client.on_message = on_message
    client.subscribe("hello_world")
    client.loop_start()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret'
mqtt_setup()


@app.route("/buttons", methods=["GET", "POST"])
def buttons():
    return render_template("buttons.html")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    return render_template("settings.html")


@app.route("/button_press", methods=["POST"])
def button_press():
    if str(request.form["button"]) == "Red":
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
    app.run(port=8000)


# this is an example
