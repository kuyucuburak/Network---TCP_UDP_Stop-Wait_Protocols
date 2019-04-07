from random import randint
from socket import *
import socket

with open('values.txt') as valuesFile:
    lines = valuesFile.readlines()
lines = [x.strip() for x in lines]
valuesFile.close()

float1 = float(lines[0].split(" ")[1])
float2 = float(lines[1].split(" ")[1])

p = 0
if float1 != 0.0:
    p = int(1 / float1)

q = 0
if float2 != 0.0:
    q = int(1 / float2)

if float1 == float2:
    r = 0
else:
    r = int(1 / (float1 - float2))

if r == 1:
    r = 2

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

socket3.settimeout(0.25)
numReceivedPocket = 0
numPacketError = 0
numBitError = 0
i = 0
while True:
    data = socket1.recv(1500)
    socket2.sendto(b'OK', (host2, port2))
    if data == b'finish':
        while True:
            try:
                socket4.sendto(data, (host4, port4))
                response = socket3.recv(1500)

                break
            except timeout:
                print("Timeout!. Sending same packet again..." + str(i))
        break

    if q != 0:
        possibilityBitError = randint(1, q)
        if possibilityBitError == 1:
            byteArrayData = bytearray()
            byteArrayData.extend(data)

            initValue = bin(byteArrayData[0])
            if byteArrayData[0] & 0b1 == 1:
                byteArrayData[0] = byteArrayData[0] ^ 1
            else:
                byteArrayData[0] = byteArrayData[0] | 1
            lastValue = bin(byteArrayData[0])

            numBitError += 1
            while True:
                try:
                    socket4.sendto(byteArrayData, (host4, port4))
                    response = socket3.recv(1500)

                    i = i + 1
                    break
                except timeout:
                    print("Timeout!. Sending same packet again..." + str(i))
            print('BIT ERROR: ' + initValue + " is changed to " + lastValue + '!')
        elif r != 0:
            possibilityPacketError = randint(1, r)
            if possibilityPacketError == 1:
                numPacketError += 1
                print('PACKET ERROR: pocket is missed!')
            else:
                while True:
                    try:
                        socket4.sendto(data, (host4, port4))
                        response = socket3.recv(1500)

                        i = i + 1
                        break
                    except timeout:
                        print("Timeout!. Sending same packet again..." + str(i))
        else:
            while True:
                try:
                    socket4.sendto(data, (host4, port4))
                    response = socket3.recv(1500)

                    i = i + 1
                    break
                except timeout:
                    print("Timeout!. Sending same packet again..." + str(i))
    elif r != 0:
        possibilityPacketError = randint(1, r)
        if possibilityPacketError == 1:
            numPacketError += 1
            print('PACKET ERROR: pocket is missed!')
        else:
            while True:
                try:
                    socket4.sendto(data, (host4, port4))
                    response = socket3.recv(1500)

                    i = i + 1
                    break
                except timeout:
                    print("Timeout!. Sending same packet again..." + str(i))
    else:
        while True:
            try:
                socket4.sendto(data, (host4, port4))
                response = socket3.recv(1500)

                i = i + 1
                break
            except timeout:
                print("Timeout!. Sending same packet again..." + str(i))

    numReceivedPocket += 1

print('Transferring file is completed.')

socket1.close()
socket2.close()
socket3.close()
socket4.close()
print('\nConnections are closed!')
