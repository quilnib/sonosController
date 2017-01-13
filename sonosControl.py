import soco
import time
import RPi.GPIO as io
io.setmode(io.BCM)

skip_pin = 24
previous_pin = 23
nothing_pin = 22

io.setup(skip_pin, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(previous_pin, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(nothing_pin, io.IN, pull_up_down=io.PUD_DOWN)
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

def previous(channel):
    print "called previous"
    sonos.previous()

def turnUp(channel):
    print "called turnUp"
    sonos.volume += 10
    
io.add_event_detect(skip_pin, io.RISING, callback=skip, bouncetime=300)
io.add_event_detect(previous_pin, io.RISING, callback=previous, bouncetime=300)
io.add_event_detect(nothing_pin, io.RISING, callback=turnUp, bouncetime=300)


while True: #This needs to be called last, since it runs forever
    time.sleep(1.0) #run for forever...

 
