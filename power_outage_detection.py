#!/usr/bin/python3 
from gpiozero import LED, Button

import time
import os

GPIOPin = 13 #Selected pin for sensing input voltage

channel = Button(GPIOPin,pull_up=False)

def Soft_Shutdown():

    print("System is Shutting Down")
    count_down_for_shutdown(6,1)
    os.system("sudo shutdown -h now")

def count_down_for_shutdown(start, stop):
	given_time = range (stop,start)
	countdown = reversed(given_time)
	for second in countdown:
	    time.sleep(1)
	    print(str(second) + '...')

if __name__ == "__main__":
	print(f'looking for power outage at GPIOpin {GPIOPin}')
	channel.wait_for_release()   
	Soft_Shutdown()                  


    
    
       

       
