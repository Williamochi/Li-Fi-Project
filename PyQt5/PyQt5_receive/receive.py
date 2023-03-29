import serial                         # add Serial library for Serial communication
import serial.tools.list_ports
import warnings

##########################arduino_setup#######################
def receive_setup():
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
    return ser

############################RECEIVE#####################################
def receive(ser, counter):                      
    if (ser.is_open == False):
        ser.open()
    RECEIVE = []
    string = ''
    while True:
        if ser.in_waiting:
            read = ser.read().decode()
            # print(read)
            RECEIVE.append(read)
            if read == '3':
                code = string.join(RECEIVE) 
                print(len(code)) 
                counter = counter + 1   
                return code, counter
    #########################DECODE######################################

   