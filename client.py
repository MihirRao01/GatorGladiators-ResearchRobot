import socket 

jetson_server = "192.168.56.1"
#jetson_server = "104.222.18.161"
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


send("Hello World!")
send("Disconnected")