import socket
import threading
from testOfMotorDrive import setMotor


# Set the IP address and port on which the Jetson Nano will listen for incoming connections
#jetson_ip = socket.gethostbyname(socket.gethostname())  
# jetson_ip = "104.222.18.161"
jetson_ip = "100.110.218.93"
jetson_port = 8000
ADDR = ('', jetson_port)

# Create a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
  

def handle_client(conn, addr):
     #print(f"Accepted connection from {addr}")
     print("Accepted Connection from :", addr )

     connected = True
     while connected:
          msg_length = conn.recv(64).decode('utf-8')
          if msg_length:
               msg_length = int(msg_length)
               msg = conn.recv(msg_length).decode('utf-8')
               if msg == "Disconnected":
                    connected = False
                    setMotor("Stop")

               #print(f"Received data:" {msg})
               print("Received data: ",msg)
               setMotor(msg)
     conn.close()           

          
     

def start():
    server.listen(5)
    while True:
          # accept incoming connections
          conn, addr = server.accept()
          thread = threading.Thread(target=handle_client, args=(conn, addr))
          thread.start()
          #print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1} ")
          print("Active Connections : ", threading.active_count()-1)
    

#print(f"Listening for connections on {jetson_ip}:{jetson_port}")
print("Listening for connections on :", jetson_ip,":",jetson_port)
start()



