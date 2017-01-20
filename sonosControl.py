import soco
import time
import RPi.GPIO as io
io.setmode(io.BCM)

skip_pin = 24
alt1_pin = 23
alt2_pin = 22

io.setup(skip_pin, io.IN, pull_up_down=io.PUD_UP)
io.setup(alt1_pin, io.IN, pull_up_down=io.PUD_UP)
io.setup(alt2_pin, io.IN, pull_up_down=io.PUD_UP)
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
    print "called skip \n"
    sonos.next()

def previous(channel):
    print "called previous \n"
    sonos.previous()

def turnDown(channel):
    print "called turnDown \n"
    sonos.volume -= 10

def turnUp(channel):
    print "called turnUp \n"
    sonos.volume += 10
    
io.add_event_detect(skip_pin, io.FALLING, callback=skip, bouncetime=300)
io.add_event_detect(alt1_pin, io.RISING, callback=turnDown, bouncetime=300)
io.add_event_detect(alt2_pin, io.RISING, callback=turnUp, bouncetime=300)


try:

    while True: #This needs to be called last, since it runs forever
        time.sleep(1.0) #run for forever...

except KeyboardInterrupt:
        io.cleanup()
 
