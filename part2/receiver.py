import socket
import time

socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host2 = socket.gethostbyname(socket.gethostname())
port2 = 64537
socket2.bind((host2, port2))

socket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host3 = socket.gethostbyname(socket.gethostname())
port3 = 64538

socket3.sendto(b"Hello server, I am receiver!", (host3, port3))

print('Waiting to receive a filename...')
data = socket2.recv(1500)
filename = "received_" + data.decode()
print('Filename is received.\n')

startTime = time.time()

with open(filename, 'wb') as f:
    print('\"' + filename + '\" named file is created!')
    while True:
        data = socket2.recv(1500)
        if not data:
            break

        f.write(data)

endTime = time.time()

f.close()
print('File is taken successfully in %0.3f seconds' % (endTime - startTime))

socket2.close()
socket3.close()
print('\nConnections are closed. Good Bye!')
