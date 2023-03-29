from time import sleep
import serial 
from pyfirmata2 import ArduinoMega
from sympy import pi
import time
import serial.tools.list_ports
import warnings

###############################arduino_setup#######################

def transmit_setup(send_array, mode):
    end ='1000000000000000000001S'
    if mode == 'L':#gry
        flag = "1010"
    else:           #RGB
        flag = "1011"
    SENDING = flag + send_array + end
    print("Searching arduino board...")
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'USB Serial' in p.description  # may need tweaking to match new arduinos
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
        board = ArduinoMega(arduino_ports[x-1], baudrate=115200)
    else:
        board = ArduinoMega(arduino_ports[0], baudrate=115200)

        
    print("Connect to ", board.name)
    blink = board.get_pin('d:7:o')# blink.write(1)

    a = len(send_array)
    print("Size to transfer:",a)
    print("Press enter to send file")
    #enter = input()
    sleep(1)
    return SENDING, blink

#######################MAIN#####################################
def transmit(SENDING, blink, count, i):
    duration = 1000000   #(ns)
    while (True):                                           #infinite loop
        #print("Start Sending")                  #prints the data for confirmation
        if(SENDING[i] == '1'):
            # print("1")
            start_time = time.monotonic_ns()
            while((time.monotonic_ns()-start_time) <= duration):
                blink.write(1)
            
        elif(SENDING[i] == '0'):
            # print("0")
            start_time = time.monotonic_ns()
            while((time.monotonic_ns()-start_time) <= duration):
                blink.write(0)
        elif SENDING[i] == '2':
            count = count + 1
            i = i + 1
            return count, i 
        else:
            print("end of sending")
            blink.write(0)
            i = i + 1
            count = count + 1
            return count, i 
        i = i + 1

    # myBytes = ser.readline().decode() 
    # print(myBytes)
    # Checks for more bytes in the input buffer
    # bufferBytes = ser.inWaiting()
    # # If exists, it is added to the myBytes variable with previously read information
    # if bufferBytes:
    #     myBytes = myBytes + ser.read(bufferBytes).decode()
    #     print(myBytes)
    
"""  
while True:                           
#print ("Start Sending")                  #prints the data for confirmation
    sleep(0.01)       
    ser.write(b'1')                     
    print ("LED ON")
    sleep(0.01)        
    ser.write(b'0')                         
    print ("LED OFF")
 """   


