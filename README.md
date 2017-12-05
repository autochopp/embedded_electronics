# embedded_electronics
The embedded part of the code for the electronics of PI2.
It should work.

In to autorun  the codes at startup, do as follows:
1. Edit your /etc/rc.local

Add this line to control the temperature:

nohup  python /home/pi/autochopp-machine/embedded_electronics/temperature/temp_control.py > /home/pi/log_temp & 

2. To run only our interface, and update data at the api

$ cd ~/.config/lxsession/LXDE-pi/
$ cp autostart autorun.bk #backupfile

Edit the autostart file, deleting all lines and writing:

@python /home/pi/autochopp-machine/main.py 
@python /home/pi/autochopp-machine/embedded_electronics/collector.py

In order to run the GPIO without root permission you'll need to 
change its ownship (Not a good practice, do it at your own risk).
