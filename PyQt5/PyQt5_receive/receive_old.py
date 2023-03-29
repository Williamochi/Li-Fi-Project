from pickle import NONE
from time import sleep
from typing import Any
import serial                         # add Serial library for Serial communication
import numpy as np
from sympy import pi
import cv2
import Def2
import time
import decode
import os
import sys
import serial.tools.list_ports
import warnings
start = time.time()
rows=256
cols=256
channels = 1
i = 0
w = 32
h = 32



##########################arduino_setup#######################
print("Searching arduino board...")
arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'CH340' in p.description  # may need tweaking to match new arduinos
]
if not arduino_ports:
    raise IOError("No Arduino found")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found please choose one of it')
    print("enter numbers to select port:",arduino_ports) 
    while True:
        try:
            x = int(input())
            if(x < len(arduino_ports)):
                break
            else:
                print("No Arduino found")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    ser = serial.Serial(arduino_ports[x-1], 115200)
else:
    ser = serial.Serial(arduino_ports[0], 115200)
print("Connect to ", ser.name)
# ser = serial.Serial(port.device, 115200)
# COM_PORT = 'COM4'
# BAUD_RATES = 115200
# ser = serial.Serial(COM_PORT, BAUD_RATES) #Create Serial port object called arduinoSerialData
#ser.bytesize = 8  
############################RECEIVE#####################################
#start = input()                   #infinite loop                           
code = '1000000000000000000001'
stop = code.encode()
start = 0
if (ser.is_open == False):
    ser.open()
print ("Start receiving")          #prints the data for confirmation
counter = 0
RECEIVE = []
RECEIVE_compare=[]
string = ''
while True:

    if ser.in_waiting:
        read = ser.read().decode()
        RECEIVE.append(read)
        if read == '3':
            print(len(RECEIVE))
            counter = counter + 1 
            # print(string)
            if counter == 4:
                break 
    # RECEIVE = ser.read_until(stop, None).decode() #有風險
    # if len(RECEIVE) > 20:
    #     print(RECEIVE)
    #     break

#########################DECODE######################################
print('End of Receiving')
print(len(RECEIVE))
colormode = RECEIVE[0:4]
if colormode == '1010':
    colormode = 'L'
else:
    colormode = 'RGB'
RECEIVE = RECEIVE[4:] + ['1']
print('End of Receiving')
print(len(RECEIVE))
rec_word = string.join(RECEIVE)
rec_word = rec_word.replace('131','')
counter = counter + 1
print(len(rec_word))
text_file = open("code.txt", "wt")
n = text_file.write(rec_word)
text_file.close()
receive_decode = decode.decode(rec_word)
decode.combine_picture(receive_decode, h ,w ,rows, cols, channels) 

