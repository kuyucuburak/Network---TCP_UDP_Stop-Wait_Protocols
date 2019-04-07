import socket
import time

# noinspection PyProtectedMember
from pip._vendor.distlib.compat import raw_input

socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host1 = socket.gethostbyname(socket.gethostname())
port1 = 64536

socket1.sendto(b"Hello server, I am sender!", (host1, port1))

filename = raw_input("Please enter the file name you want to sent: ")
f = open(filename, 'rb')
read = f.read(1500)
socket1.sendto(bytes(filename, encoding="UTF-8"), (host1, port1))

startTime = time.time()

print('\nFile is being started to sent...')
while read:
    socket1.sendto(read, (host1, port1))
    read = f.read(1500)
socket1.sendto(read, (host1, port1))

endTime = time.time()

f.close()
print('File is sent successfully in %0.3f seconds' % (endTime - startTime))

socket1.close()
print('\nConnection is closed. Good Bye!')
