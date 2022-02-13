#todo: make this into a nice class. 

import paho.mqtt.client as paho


class LEDMessager:
    def __init__(self, username, password, topic="LED"):
        self.broker = "ledmqtt.devsoft.co.za"
        # self.broker = "159.65.184.34"
        self.port = 1883
        self.username = username
        self.password = password
        self.topic = topic
        #set up paho service:
        self.client = paho.Client(self.username + self.topic) #this is just a name for the instance
        self.client.username_pw_set(self.username, self.password)
        self.client.on_message=self.__on_message

    #define callback - todo: this is not implemented properly yet. 
    def __on_message(self, client, userdata, message):
        print("received message: ",str(message.payload.decode("utf-8")))
        return(str(message.payload.decode("utf-8")))
    
    def connect(self):        
        print("connecting to broker ")
        self.client.connect(self.broker,self.port)#connect
        self.client.loop_start() #start loop to process received messages
        print("subscribing to ", self.username + "/" + self.topic)
        self.client.subscribe(self.username + "/" + self.topic)#subscribe
    
    def send(self):
        print("publishing ")
        self.client.publish(self.username + "/" + self.topic, "on")#publish
        
    def close(self):
        self.client.disconnect() #disconnect
        self.client.loop_stop() #stop loop


#test:                
# mClient = LEDMessager("abcdefghij", "klmnopqrst", "RED") # initialise for paid version
# 
# mClient = LEDMessager("abcdefghij", "klmnopqrst") #initialise for free version "LED"
#
# mClient.connect()
# mClient.send()
# mClient.close()

