import socket
import time

socket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host3 = socket.gethostbyname(socket.gethostname())
port3 = 64328

socket4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host4 = socket.gethostbyname(socket.gethostname())
port4 = 64329
socket4.bind((host4, port4))

socket3.sendto(b"Hello server, I am receiver!", (host3, port3))

print('Waiting to receive a file...\n')
filename = "received_" + socket4.recv(1500).decode()

startTime = time.time()
with open(filename, 'wb') as f:
    print('\"' + filename + '\" named file is created!')
    while True:
        data = socket4.recv(1500)
        socket3.sendto(b'OK', (host3, port3))

        if data == b'finish':
            break

        f.write(data)

endTime = time.time()

f.close()
print('File is taken successfully in %0.3f seconds' % (endTime - startTime))

socket3.close()
socket4.close()
print('\nConnection is closed. Good bye!')
