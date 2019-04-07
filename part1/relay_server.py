import socket

port1 = 60324
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host1 = socket.gethostbyname(socket.gethostname())
socket1.bind((host1, port1))           
socket1.listen(5)

port2 = 60325
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host2 = socket.gethostbyname(socket.gethostname())
socket2.bind((host2, port2))           
socket2.listen(5)

print('Server started to listen sender and receiver...')

conn1, address1 = socket1.accept()
data = conn1.recv(1500)
print('Sender has connected: \"' + data.decode() + "\"")

conn2, address2 = socket2.accept()
data = conn2.recv(1500)
print('Receiver has connected: \"' + data.decode() + "\"")

data = conn1.recv(1500)
print("\nStarting to transfer " + data.decode() + " named file.")
conn2.send(data)

hashValue = conn1.recv(32)
print('Transferring the hash value: ' + hashValue.decode())
conn2.send(hashValue)

while True:
    data = conn1.recv(1500)
    conn2.send(data)
    
    if not data:
        break

print('Transferring file is completed.')
print('\nConnections are closed. Good Bye!')
conn1.close()
conn2.close()
