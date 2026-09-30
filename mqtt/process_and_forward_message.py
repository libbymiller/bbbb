import paho.mqtt.client as mqtt #import the client1
import time
import json
import traceback
import base64
import random
import paho.mqtt.publish as publish


def on_message(client, userdata, message):

    print("got msg",message)

    try:

      decoded_message=str(message.payload.decode("utf-8"))
      msg=json.loads(decoded_message)
      print("msg",msg)

      #pl = msg["uplink_message"]["frm_payload"]

      #print("message payload=",pl,"decoded",base64.b64decode(pl))
      #thing = base64.b64decode(pl)
      #dt = msg["received_at"];
      #print("thing",thing)
      #bird = str(thing).split("_")
      #pay = {"species":bird[0],"confidence":bird[1],"date_time":dt}

      publish.single("boids", json.dumps(msg), hostname="XXXXask libbyXXXX", port=1883)

      print("published")
    except Exception as e: 
      print(e)
      print("Exception")
      traceback.print_exc()

broker_address="localhost"

print("creating new instance")

r = random.randint(1000, 9999)

client_n = "wifi_"+str(r) #must be unique or it breaks weirdly
#client = mqtt.Client("P2") #create new instance
#client = mqtt.Client(client_n) #create new instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_n) #create new instance

client.on_message=on_message #attach function to callback

print("connecting to broker")

client.connect(broker_address, 1883) #connect to broker

tpic = "boids"

print("Subscribing to topic",tpic)
client.subscribe(tpic)

client.loop_forever()
