from socket import *
import socket

socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host1 = socket.gethostbyname(socket.gethostname())
port1 = 64326
socket1.bind((host1, port1))

socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host2 = socket.gethostbyname(socket.gethostname())
port2 = 64327

socket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host3 = socket.gethostbyname(socket.gethostname())
port3 = 64328
socket3.bind((host3, port3))

socket4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host4 = socket.gethostbyname(socket.gethostname())
port4 = 64329

print('Server started to listen sender and receiver...')

data = socket1.recv(1500)
print('Sender has connected: \"' + data.decode() + "\"")

data = socket3.recv(1500)
print('Receiver has connected: \"' + data.decode() + "\"")

data = socket1.recv(1500)
print("\nStarting to transfer " + data.decode() + " named file.")
socket4.sendto(data, (host4, port4))

socket3.settimeout(0.01)
i = 0
while True:
    data = socket1.recv(1500)
    socket2.sendto(b'OK', (host2, port2))

    while True:
        try:
            socket4.sendto(data, (host4, port4))
            response = socket3.recv(1500)

            i = i + 1
            break
        except timeout:
            print("Timeout!. Sending same packet again..." + str(i))

    if data == b'finish':
        break

print('Transferring file is completed.')

socket1.close()
socket2.close()
socket3.close()
socket4.close()
print('\nConnections are closed!')
