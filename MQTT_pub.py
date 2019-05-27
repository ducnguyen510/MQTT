import paho.mqtt.client as mqtt
import time
import logging
broker = "192.168.1.76"
port =1883
global data
data ="001-89-34"

logging.basicConfig(level=logging.INFO)
def on_log(client, userdata, level, buf): #tao nhat ki phien lam viec
    logging.info(buf)
def on_connect(cllient, userdata , flags, rc): #tao ket noi
    if rc ==0:
        client.connect_flag =True #set flag
        logging.info("connected OK")
    else:
        logging.info("Bad connection retured code"+str(rc))
        client.loop_stop()
def on_disconnect(client, userdata,rc):     # tao ngat ket noi
    logging.info("client disconnect ok")

def on_publish(client, userdata,mid):    # tao 1 publish
    logging.info("In on_pub callback mid"+str(mid))
def reset():         #reset
    ret = client.publish("humidity","",0,True)
def on_subscribe(client,userdata,mid,granted_qos): #tao 1 subcribe
    logging.info("subscribe")
def on_message(client,userdata,message):      #xem thong tin message
    topic=message.topic
    msgr =str(message.payload.decode("utf-8"))
    msgr ="message received " +msgr
    logging.info(msgr)

def tokenline():
   global data1
   global temp
   global humi
   data1 =data.split("-")
   temp = int(data1[2])
   humi = int(data1[1])



mqtt.Client.connect_flag =False      #set retain =False
client = mqtt.Client("python 1") #creat new instance
client.on_log =on_log
client.on_connect =on_connect#bind call back function
client.on_disconnect =on_disconnect
client.on_publish=on_publish
client.on_subscribe=on_subscribe
client.on_message =on_message


client.connect(broker,port)       #establish connection
client.loop_start()

while not client.connect_flag: #wait in loop
    logging.info("in wait loop")
    time.sleep(1)
time.sleep(3)

while(1):
 tokenline()
 logging.info("publishing")
 ret =client.publish("humidity",humi,0) #publish
 logging.info("publish return"+str(ret))
 time.sleep(3)
 #client.loop()
 ret =client.publish("temperature",temp,1) #publish
 logging.info("publish return"+str(ret))
 time.sleep(3)
 #client.loop()
 ret =client.publish("humidity","85",2) #publish
 logging.info("publish return"+str(ret))
 time.sleep(3)
 client.subscribe("humidity")
 time.sleep(1)
 #client.loop()Unique
time.sleep(3)

#reset()
time.sleep(4)
client.loop_stop()
client.disconnect()


