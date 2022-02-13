 
# LED Indicator Messager
![LED Indicator Messager](https://github.com/tomjuggler/led_indicator_messager/blob/main/assets/banner-772x250.png?raw=true)
Convenient python library used to send messages to LED Website Indicator MQTT service
<br>
Requires a free or paid subscription to LED Website Indicator service
<br>
See [LED Website Indicator website](http://ledindicator.devsoft.co.za) to sign up. 
<br>
## Usage: 
    #initialise:
    #mClient = LEDMessager(<username>, <password>, <colour>)
    mClient = LEDMessager("abcdefghij", "klmnopqrst", "RED") #paid version
    mClient = LEDMessager("abcdefghij", "klmnopqrst") #free version without colours
    #use:
    mClient.connect()
    mClient.send()
    mClient.close()
<br>
## TODO:
Callbacks not implemented yet, just sending - which is good for most use cases..

