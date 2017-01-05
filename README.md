# sonosController
A simple button-activated controller for the office Sonos.

Add a line to the end of the ~/.config/lxsession/LXDE-pi/autostart file to call the python file which launches on boot. Currently that looks like:

"python /home/pi/Documents/sonos/sonosController.py"

update the sonosController.py file to be executable without "sudo" by doing a "sudo chmod 755 sonosController.py"
