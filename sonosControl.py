import soco
import time
import RPi.GPIO as io
io.setmode(io.BCM)

button_pin = 24
io.setup(button_pin, io.IN, pull_up_down=io.PUD_DOWN)
sonos = None
deviceName = "East"

for device in soco.discover():
    if device.player_name == deviceName:
        sonos = device
        print sonos.player_name
        break
    else:
        device = None        

def skip(channel):
    print "called skip"
    sonos.next()
    
io.add_event_detect(button_pin, io.RISING, callback=skip, bouncetime=300)

while True: #This needs to be called last, since it runs forever
    time.sleep(1.0) #run for forever...

 
