import serial
'''
class SerialArduino:
    def __init__(self):
        
        get_inputbtn = int(input('input 0 to start: '))
        if get_inputbtn== 0:
            ser = serial.Serial('COM3',  baudrate=115200)
        while True and get_inputbtn== 0:
            line = ser.readline()
            self.check_inf(line)
        ser.close()
    
    def check_inf(self, input_inf):
        if input_inf != b'':
            get_cm = str(input_inf).split("'")[1].split("\\")[0]
            print('input_inf: ',get_cm)

if __name__ == '__main__':
    try:
        SerialArduino()
    except KeyboardInterrupt:
        print("Shutting down")
'''
a = '12345600000000000000000000'
b = '00000000000000000000'

print()
#print(a[:-20])