import paho.mqtt.client as mqtt 

def publish(topic, content)
    # The callback for when the client receives a CONNACK response from the server. 
    def on_connect(client, userdata, flags, rc): 
    	print("Connected with result code "+str(rc)) 

    	# Subscribing in on_connect() means that if we lose the connection and 
    	# reconnect then subscriptions will be renewed. 
    	client.subscribe("section1") 

    # The callback for when a PUBLISH message is received from the server. 
    def on_message(client, userdata, msg): 
    	print(msg.topic+" "+str(msg.payload)) 

     # Create an MQTT client and connect to HiveMQ broker  
    client = mqtt.Client() 
    client.on_connect = on_connect 
    client.on_message = on_message 

     # Connect to the HiveMQ broker  
    client.connect("broker.hivemq.com", 1883, 60) 

     # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.   # Other loop*() functions are available that give a threaded interface and a manual interface.  
    client.loop_start()  

     # Publish "section1" to HiveMQ broker  
    client.publish(str(topic), str(content))
