Network - TCP, UDP, Stop&Wait Protocols
=======================================

### Introduction
This project is created for implementing TCP and UDP protocols.

### How to use?
The all parts works in the same way. There are three python files for the _"part1"_, _"part2"_, _"part3"_ and _"part4"_.

1. **relay_server.py:** This is a server.
2. **sender.py:**  This is a sender which sends _"picture.jpg"_.
3. **receiver.py:** This is a receiver which receives _"picture.jpg"_.

Follow the following steps to use the program:

1. Run _"relay_server.py"_.
2. Run _"sender.py"_.
3. Run _"receiver.py"_.

Then, output of the _"relay_server.py"_ will be like the following:
>**Server started to listen sender and receiver...<br>
Sender has connected: "Hello server, I am sender!"<br>
Receiver has connected: "Hello server, I am receiver!"**<br>

Enter _"picture.jpg"_ for the "sender.py". It will be like the following:
>**Please enter the file name you want to sent:** picture.jpg

Then, processes will be completed.

### Overview
When processes are completed, _"received_picture.jpg"_ is created as a result for the all parts. However, size and quality of the _"received_picture.jpg"_ differs according to protocols.

**Part 1**<br>
This is an implementation of the TCP protocol. Size of the _"received_picture.jpg"_ is the same as _"picture.jpg"_. Because, TCP protocol is reliable.

_"picture.jpg"_<br>(picture size = 384.81 kB) | _"received_picture.jpg"_<br>(picture size = 384.81 kB)
--------------------------------------------- | ------------------------------------------------------
![Image](extras/1.jpg)                 | ![Image](extras/1.jpg)

As seen in the example, sizes of the _"picture.jpg"_  and _"received_picture.jpg"_ are exactly the same.

**Part 2**<br>
This is an implementation of the UDP protocol. Size of the _"received_picture.jpg"_ is usually not the same as _"picture.jpg"_. Because, UDP protocol is not reliable. Because of packet losses, size of the _"received_picture.jpg"_ is lower than the size of the _"picture.jpg"_. Therefore, _"received_picture.jpg"_ is a damaged image. 

_"picture.jpg"_<br>(picture size = 384.81 kB) | _"received_picture.jpg"_<br>(picture size = 371.31 kB)
-------------------------------------------- | ------------------------------------------------------
![Image](extras/1.jpg)                | ![Image](extras/2.jpg)

As seen in the example, sizes of the _"picture.jpg"_  and _"received_picture.jpg"_ are not the same. Size of the _"received_picture.jpg"_ is lower. Because some of the packets did not reach to the receiver because of unreliability of the UDP protocol.

**Part 3**<br>
This is an implementation of the _"stop & wait"_ protocol by using UDP. This is reliable, because _"stop & wait"_ protocol sending same packet until getting _"OK"_ message from the receiver.

_"picture.jpg"_<br>(picture size = 384.81 kB) | _"received_picture.jpg"_<br>(picture size = 384.81 kB)
--------------------------------------------- | ------------------------------------------------------
![Image](extras/1.jpg)                 | ![Image](extras/1.jpg)

As seen in the example, size of the sent and received pictures are exactly the same. Because reliability is provided by _"stop & wait"_ protocol.

**Part 4**<br>
This is an implementation of the _"stop & wait"_ protocol by using UDP. However, there is one difference from the _"part3"_. There are _"p"_ and _"q"_ values between 0-1 which is taken from the _"values.txt"_ file. _"p"_ value represents the packet drop and error rate and _"q"_ value represents the bit error rate. _"q"_ is a subset of the _"p"_ . Because if there is a bit error, it is also a packet error.

_"picture.jpg"_<br>(picture size = 384.81 kB)              | _"received_picture.jpg"_<br>(picture size = 384.81 kB)<br>(p=0.1, q=0.1)<br>    | _"received_picture.jpg"_<br>(picture size = 307.50 kB)<br>(p=0.3, q=0.1)
----------------------------- | ------------------------------------------ | ---------------------------------------
![Image](extras/1.jpg) | ![Image](extras/3.jpg)              | ![Image](extras/4.jpg)

As seen in the examples, there are two tries.
1. Sizes of the _"picture.jpg"_ and the first _"received_picture.jpg"_ are exactly the same. Because, there is no packet loss. They are calculated as the following:<br>
_**Bit error:**_ q = 0.1 = %10<br>
_**Packet error:**_ p = 0.1 = %10<br>
_**Packet drop:**_ p - q = 0.1 - 0.1 = 0 = %0<br>

2. Sizes of the _"picture.jpg"_ and the second _"received_picture.jpg"_ are not the same. Because, there is %20 packet loss. They are calculated as the following:<br>
_**Bit error:**_ q = 0.1 = %10<br>
_**Packet error:**_ p = 0.3 = %30<br>
_**Packet drop:**_ p - q = 0.3 - 0.1 = 0.2 = %20<br>

### License
Copyright 2019 Burak Kuyucu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


