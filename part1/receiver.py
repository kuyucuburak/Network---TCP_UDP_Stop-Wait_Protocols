import hashlib
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port_relayServer = 60325

s.connect((host, port_relayServer))
s.send(b"Hello server, I am receiver!")

print('Waiting to receive a filename...')
filename = "received_" + s.recv(1500).decode()
print('File name is taken.\n')

startTime = time.time()

print('Waiting to receive a hash value...')
hashValue = s.recv(32)
print("Hash value is taken: " + hashValue.decode() + "\n")

with open(filename, 'wb') as f:
    print('\"' + filename + '\" named file is created!')
    while True:
        data = s.recv(1500)
        if not data:
            break

        f.write(data)
print('\"' + filename + '\" named file is received!')

hashing = hashlib.md5()
with open(filename, 'rb') as aFile:
    buf = aFile.read()
    hashing.update(buf)

newFileHashValue = hashing.hexdigest()
print("\nReceived file's hash value: " + newFileHashValue)
if hashValue == newFileHashValue:
    print('Hash values are equal. File is taken reliably!')
else:
    print('Hash values are not equal. File is wrong!!')

endTime = time.time()

f.close()
print('\nFile is taken successfully in %0.3f seconds' % (endTime - startTime))

s.close()
print('\nConnection is closed. Good Bye!')
