import socket
import time

# noinspection PyProtectedMember
from pip._vendor.distlib.compat import raw_input

socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host1 = socket.gethostbyname(socket.gethostname())
port1 = 64326

socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host2 = socket.gethostbyname(socket.gethostname())
port2 = 64327
socket2.settimeout(0.25)
socket2.bind((host2, port2))

socket1.sendto(b"Hello server, I am sender!", (host1, port1))

filename = raw_input("Please enter the file name you want to sent: ")
f = open(filename, 'rb')
read = f.read(1500)
socket1.sendto(bytes(filename, encoding="UTF-8"), (host1, port1))

startTime = time.time()
i = 0
while read:
    try:
        socket1.sendto(read, (host1, port1))

        response, address = socket2.recvfrom(1500)

        read = f.read(1500)
        i = i + 1
    except socket.timeout:
        print("Timeout!. Sending same packet again..." + str(i))

socket1.sendto(b'finish', (host1, port1))
finishCall = socket2.recv(4096)
endTime = time.time()

f.close()
print('\nFile is sent successfully in %0.3f seconds' % (endTime - startTime))

socket1.close()
socket2.close()
print('\nConnection is closed. Good bye!')
