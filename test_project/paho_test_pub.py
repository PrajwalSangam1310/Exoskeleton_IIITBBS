import paho.mqtt.client as paho
import sys
import numpy as np

# @datatype
# class points:
#     a1: float

def onMessage(client, userdata, msg):
    print(msg.topic+": "+ msg.payload.decode('utf-8'))
    print(msg.payload)
    print(np.frombuffer(msg.payload,dtype=np.float32,count=1))

    # print(np.array(msg.payload, dtype = np.float32))

client = paho.Client()
client.on_message = onMessage

if client.connect("192.168.13.251", 1883, 60) !=0:
    print("couldnt connect to the brker, exititng")
    sys.exit(-1)

# client.subscribe("/RIGHT_THIGH/command_data")

example_float_data = np.array([6.0,2.0,5.0], dtype=np.float32).tobytes()
print(len(example_float_data))
example_int_data = np.array([2.0,1.0], dtype=np.int32).tobytes()
print(len(example_int_data))
send_data  = example_float_data + example_int_data

client.publish("/RIGHT_THIGH/command_data", send_data,0)

try:
    print("press ctrl+c to stop the execution")
    client.loop_forever()
except:
    print("Disconnected from the server")

client.disconnect()