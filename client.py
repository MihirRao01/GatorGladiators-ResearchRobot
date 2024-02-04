import socket
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial("/dev/cu.usbmodem14301", 9600)

# jetson_server = "192.168.56.1"
# jetson_server = "104.222.18.161"
jetson_server = "100.110.218.93"
jetson_server_port = 8000
ADDR = (jetson_server, jetson_server_port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(data):
    msg = data.encode('utf-8')
    msg_length = len(msg)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' '*(64-len(send_length))
    client.send(send_length)
    client.send(msg)


send("Hello JetsonNano!")

while True:
    try : 
        if serialInst.in_waiting:
            packet = serialInst.readline()
            print(packet.decode('utf'))
            send(packet.decode('utf'))
    except:
        send("Disconnected")
        break
