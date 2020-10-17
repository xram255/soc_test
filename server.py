from time import sleep as delay
import socket

PORT = 5050
#SERVER = "192.168.8.100"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
ip = socket.gethostbyname('www.google.com')

print("wait...")
delay(2)
print(SERVER, "  ", socket.gethostname(), "  ", ip)