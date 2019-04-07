import hashlib
import socket
import time

# noinspection PyProtectedMember
from pip._vendor.distlib.compat import raw_input

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host1 = socket.gethostbyname(socket.gethostname())
port1 = 60324
socket1.connect((host1, port1))

socket1.send(b"Hello server, I am sender!")

filename = raw_input("Please enter the file name you want to sent: ")
f = open(filename, 'rb')
read = f.read(1500)
print('\nFile name is being sent...')
socket1.send(bytes(filename, encoding="UTF-8"))

startTime = time.time()

print('Hash value is being sent...')
hashing = hashlib.md5()
with open(filename, 'rb') as aFile:
    buf = aFile.read()
    hashing.update(buf)

socket1.send(bytes(hashing.hexdigest(), encoding="UTF-8"))
print('Hash value is sent...')

while read:
    socket1.send(read)
    read = f.read(1500)
socket1.send(read)

endTime = time.time()

f.close()
print('File is sent successfully in %0.3f seconds' % (endTime-startTime))

socket1.close()
print('\nConnection is closed. Good Bye!')
