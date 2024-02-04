import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial("/dev/cu.usbmodem14301",9600)

while True:
    if serialInst.in_waiting: 
        packet = serialInst.readline()
        print(packet.decode('utf-8'))