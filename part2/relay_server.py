import socket

port1 = 64536
socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host1 = socket.gethostbyname(socket.gethostname())
socket1.bind((host1, port1))

port2 = 64537
socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host2 = socket.gethostbyname(socket.gethostname())

port3 = 64538
socket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host3 = socket.gethostbyname(socket.gethostname())
socket3.bind((host3, port3))

print('Server started to listen sender and receiver...')

data, address1 = socket1.recvfrom(1500)
print('Sender has connected: \"' + data.decode() + '\"')

data, address2 = socket3.recvfrom(1500)
print('Receiver has connected: \"' + data.decode() + "\"")

text, address3 = socket1.recvfrom(1500)
print("\nStarting to transfer " + text.decode() + " named file.")
socket2.sendto(text, (host2, port2))

while True:
    data, address4 = socket1.recvfrom(1500)
    socket2.sendto(data, (host2, port2))

    if not data:
        break

print('Transferring file is completed.')

socket1.close()
socket2.close()
socket3.close()
print('\nConnections are closed. Good Bye!')
