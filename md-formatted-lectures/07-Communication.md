## Communication


# Communications


- Connection-oriented service

     - Before exchanging data, the sender and receiver first explicitly establish a connection, and
possibly negotiate specific parameters of the protocol they will use


- Connectionless service

     - No setup in advance is required. The sender just transmits the first message when it’s ready.


# Communications


- Layered protocols

- ISO OSI (Open Systems
Interconnection) reference model

    - Layers

    - Interfaces

    - Protocols

       - Protocol suite/stack


- Connection-oriented vs connectionless


# Message encapsulation


# OSI and TCP/IP


# Communications

#### Application layer


- Applications

- Application-specific and general-purpose
protocols

- E.g., FTP, HTTP(S), SMTP, _RTSP, SIP, SNMP_


#### Transport layer


- Logical end-to-end comm. between
processes


- Multiplexing of segments at sender,
demultiplexing of segments at receiver


- Reliable vs unreliable, connectionoriented vs connectionless, (un)ordered

- Acknowledgement


- E.g., TCP, UDP, _RTP, SCTP_


# Communications

#### Network layer


- Logical comm. between hosts,
(inter)networking


- Routing and forwarding of
datagrams/segment


- Multi-node networking, addressing,
routing and traffic control

- Like a map


- E.g., IPv4, IPv6


#### Data link layer


- Transmission of data frames over a link

- Transmission and switching


- Like a road sign

- E.g., IEEE 802 protocol family (Ethernet,
WLAN, WiMAX, Bluetooth, Wi-Fi), MAC


# Communications

#### Physical layer


- Cables. Think physical stuff.

- E.g., copper, fiber, radio, coax


# OSI layers









|Layer|Col2|Col3|Protocol data<br>unit (PDU)|Function|
|---|---|---|---|---|
|Host<br>layers|7|Application|Data|High-level protocols such as for resource sharing or remote file access,<br>e.g. HTTP.|
|Host<br>layers|6|Presentation|Presentation|Translation of data between a networking service and an application;<br>including character encoding, data compression and encryption/decryption.|
|Host<br>layers|5|Session|Session|Managing communication sessions, i.e., continuous exchange of information in<br>the form of multiple back-and-forth transmissions between two nodes.|
|Host<br>layers|4|Transport|Segment, Datagram|Reliable transmission of data segments between points on a network,<br>including segmentation, acknowledgement and multiplexing.|
|Media<br>layers|3|Network|Packet|Structuring and managing a multi-node network,<br>including addressing, routing and traffic control.|
|Media<br>layers|2|Data link|Frame|Transmission of data frames between two nodes connected by a physical layer.|
|Media<br>layers|1|Physical|Bit, Symbol|Transmission and reception of raw bit streams over a physical medium.|


[Source: https://en.wikipedia.org/wiki/OSI_model](https://en.wikipedia.org/wiki/OSI_model)


# Middleware protocols

Session + presentation → Middleware

- Additional services between application and OS


- Security protocols for authentication and authorization

- Commit protocols for transaction management


- Locking protocols for concurrency management

- Comm. protocols (remote procedure call, remote method invocation, stream
management)


- E.g., libraries, game engines


# Middleware protocols


# Persistent / transient


- Persistent

    - Messages are stored in the middleware

    - … for as long as it takes to deliver message

    - Like email/SMS: You can read it when you have the time


- Transient

    - Messages are not stored in the middleware

    - Like a phone call: You must be available when getting the call


# Async / sync


- Async

    - Think multi-threaded! Or having sent an email.

    - Sender can continue working right after having sent the message.


- Sync

    - Think single-threaded. Or calling somebody.

    - Sender (caller) must wait for a reply.


# Discrete / streaming


- Discrete

    - Messages are part of a whole message, all of which must be sent.

    - Like downloading a video.


- Streaming

    - Not all messages must make it.

    - Like streaming a video. Missing a single frame is acceptable.


# Client-server Architecture


- Generally transient synchronous communication

    - The Client-Server communication is active

    - Server does not ask – client does

    - Server is just waiting for orders to do (which is why it’s called a server)


- Drawbacks of sync comm.

  - Client is blocked when waiting for reply

  - Requests and failures must be dealt with quickly

  - Not suitable for e.g. mail and news


# Communications

### • Message-oriented transient communication: Berkeley sockets • TCP socket primitives • Connection-oriented communication pattern using sockets



**16**


# Sockets in Python

#### Client

from socket import 

s = socket(AF_INET, SOCK_STREAM)


s.connect((HOST, PORT))


s.send('Hello, world!')


data = s.recv(1024)


print(data)


s.close()


#### Server

from socket import 

s = socket(AF_INET, SOCK_STREAM)


s.bind((HOST, PORT))


s.listen(1)


(conn, addr) = s.accept()


while True:


data = conn.recv(1024)


if not data:


break


conn.send(data)


conn.close()


# Cryptography

#### Symmetric


- One key

- Often faster


- Encrypting and sharing data


#### Asymmetric (public-key)


- Two keys

- Often slower


- Key exchange, signing and certificates


## APIs

REST, RPC and more


# Types of APIs


# Simple API example

```
CONTACTS = [{"name": "Paul"}, {"name": "Mary"}, {"name": "John"}]

@app.get('/contacts’)

def get_contacts():

return CONTACTS

@app.get('/contacts/{item_id}’)

def get_contacts(item_id):

item = ... # Find the correct item

return item

```

