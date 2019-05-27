import paho.mqtt.client as mqtt
import time
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

print("Raspberry's sending : ")

try:
    while True:
        ser.write(b'hehe')
        ser.flush()
        print("hehe")
        time.sleep(1)
except KeyboardInterrupt:
    ser.close()
def on_log(client, userdata, level, buf):
    print("log:" +buf)
def on_connect(cllient, userdata , flags, rc):
    if rc ==0:
        print ("connected OK")
    else:
        print("Bad connection retured code",rc)
def on_disconnect(client, userdata ,flags ,rc=0):
    print ("Disconnected result code"+str(rc))
def on_message(client ,userdata,msg):
    topic =msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("message received",m_decode)
broker = "192.168.1.76"
client = mqtt.Client("python 1") #creat new instance

client.on_connect =on_connect#bind call bback function
client.on_disconnect =on_disconnect
client.on_log =on_log
client.on_message=on_message

print ("connecction to broker",broker)

client.connect(broker) #connect to broker

client.loop_start()# start loop
client.subscribe("humidity") # doc ban tin
client.publish("humidity","90")


time.sleep(4)
client.loop_stop()#stop loop

client.disconnect()#disconnect