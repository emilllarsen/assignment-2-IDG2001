# CLOUD TECH RECAP
IDG2001 summary lecture
1
Regarding the exam
■ It will be available in English
■ Questions will probably be a mix of multiple-choice, discussion/explanation and
```
some code/language questions (e.g., what does the following Python code do).
```
Similar to last year.
■ When making the exam, I am also planning on sending out exam-like questions, so
you’ll have an idea what to expect.
2
1
Cloud Tech Basics
3
Lecture 01 – Cloud Tech Basics
```
Definitions Cloud basics History (?)
```
Cloud Service
```
Model (PaaS++)
```
Private, public and
```
hybrid Payment models (?)
```
Distributed
computing/systems
Systems, admins,
devops, CI/CD, APIs,
words
Pros/cons
Computing and software resources that
are delivered on demand as service.
4
Lecture 01 –
Cloud Tech
Basics
5
Lecture 01 –
Cloud Tech
Basics
6
LECTURE 01 – CLOUD TECH BASICS
Self-hosting server IaaS PaaS SaaS
78
Lecture 01 – Cloud Tech Basics
9
Lecture 01 –
Cloud Tech
Basics
10
Lecture 01 – Cloud
Tech Basics
```
■ The Big (IaaS+PaaS) providers:
```
– AWS - Amazon Web Services
– MS Azure - Microsoft’s thingy
– GCP - Google Cloud Platform
■ Allows you to host both IaaS and PaaS
systems
■ OpenStack provides similar services, but as
```
FOSS (Free Open-Source Software) :D
```
■ Other IaaS and PaaS providers exist – like
```
Railway.app and Render (both PaaS)
```
11
2
Python
12
Lecture 02 - Python
■ Easy to learn and yet among the most popular and sought after languages
■ Often used IDEs: VS Code, PyCharm, JupyterHub/-Lab, Google Colab, Spyder ++
■ Indent is what defines code blocks
■ Install modules using pip
■ Import modules using “import x” or “from x import y”
■ Can use tools like flake8, black, mypy, pytest and tox ++ to check code quality
13
Lecture 02 - Python
```
■ Interpreted (not compiled)
```
```
■ Uses indentation instead of brackets (like yaml)
```
■ File extension: .py
14
Lecture 02 - Python
```
def f(x):
```
return 2 * x
```
print(f(3))
```
```
def g(x, y):
```
```
a = x * y
```
```
b = x y
```
return a b
```
def h(x, y=1):
```
if y == 0:
return None
return x / y
class FilePath:
```
def __init__(self, location, filename, extension):
```
self.location = location
self.filename = filename
self.extension = extension
```
def get_full_path(self):
```
```
return f'{self.location}/{self.filename}.{self.extension}'
```
```
def change_name(self, new_name):
```
self.filename = new_name
15
Lecture 02 - Python
■ Learn Python in X Minutes: https://learnxinyminutes.com/docs/python/
16
3
Client-Server Architecture
17
Lecture 03 – Client-Server Architecture
Design considerations
■ Distribution transparency
■ Openness
■ Failures
```
■ Scalability (geographical and administrative)
```
■ Techniques for scaling:
– Loose coupling of the components
– Stateless design
– Database choice and design
– Async communication
– Replication and caching
18
Lecture 03 – Client-Server Architecture
Transparency Description
Access Hide differences in data representation and how an object is accessed
Location Hide where an object is located
Relocation Hide that an object may be moved to another location while in use
Migration Hide that an object may move to another location
Replication Hide that an object is replicated
Concurrency Hide that an object may be shared by several independent users
Failure Hide the failure and recovery of an object
19
Lecture 03 – Client-Server Architecture
Architectures
■ Software vs system architecture
■ Components and connectors
■ Layered, object-based, data-centered, event-based
20
Lecture 03 – Client-
Server Architecture
Layered architectures
2122
Lecture 03 –
Client-Server
Architecture
Object-based architectures
23
Lecture 03 – Client-Server Architecture
Layered architectures
Database
with Web pages
Query
generator
Ranking
algorithm
HTML
generator
User interface
Keyword expression
Database queries
Web page titles
with meta-information
Ranked list
of page titles
HTML page
containing list
Processing
level
User-interface
level
Data level
24
Lecture 03 – Client-Server Architecture
Data-centered architectures
Operation Description
POST Create a new resource
GET Retrieve the state of a resource in some representation
DELETE Delete a resource
PUT Modify a resource by transferring a new state
25
Lecture 03 – Client-Server Architecture
Event-based architectures
26
Lecture 03 –
Client-Server
Architecture
Web architecture
27
Lecture 03 – Client-
Server Architecture
Architectures
■ Centralized and decentralized
■ Multi-tiered architectures
28
Lecture 03 –
Client-Server
Architecture
29
4
Process, Virtualization and Communications
30
Lecture 04 – Process, Virtualization
and Communications
Process vs thread
■ A task can use 1 or more process
■ A process can use 1 or more threads
■ Thread context switching is managed by the program/process
■ Process context switching is managed by the operating system
■ Process switching is slow thread switching is fast
■ Process parallelism is “more” parallel
31
Lecture 04 – Process, Virtualization and Communications
32
Lecture 04 –
Process,
Virtualization and
Communications
Virtualization
■ An interface between host system and
subsystem.
■ E.g. VMs, Docker, emulator, etc.
33
5
Communication and APIs
34
Lecture 05 -
Communication and
APIs
■ Connection-oriented vs connectionless
```
■ ISO OSI (and similar models)
```
35
Lecture 05 - Communication and APIs
Layer Protocols
5. Application FTP, HTTP, SMTP, (RTSP, SIP, SNMP)
4. Transport TCP, UDP, (RTP, SCTP)
3. Network IPv4, IPv6
2. Data link IEEE 802 family. Ethernet, WLAN, WiMAX
1. Physical Fiber, copper, radio, coax, electromagnetic radiation
36
Lecture 05 - Communication and APIs
■ Persistent vs transient
– Is the data kept or deleted after sending? E.g. sms/mail vs phone call
```
■ Async vs sync (Downsides of sync: Client is blocked during communication.)
```
```
■ Discrete (e.g. TCP) vs streaming (e.g. UDP)
```
■ Client-server
– Generally transient synchronous communication
– Master-slave system, where client is master and server is slave
3738
Lecture 05 -
Communication
and APIs
Lecture 05 - Communication and APIs
# Server
from socket import *
```
s = socket(AF_INET, SOCK_STREAM)
```
```
s.bind((HOST, PORT))
```
```
s.listen(1)
```
```
(conn, addr) = s.accept()
```
while True:
```
data = conn.recv(1024)
```
if not data:
break
```
conn.send(data)
```
```
conn.close()
```
39
Lecture 05 - Communication and APIs
# Client
from socket import *
```
s = socket(AF_INET, SOCK_STREAM)
```
```
s.connect((HOST, PORT))
```
```
s.send('Hello, world!')
```
```
data = s.recv(1024)
```
```
print(data)
```
```
s.close()
```
40
Lecture 05 - Communication and APIs
41
Lecture 05 - Communication and APIs
Communication related data structures / files types
■ JSON
■ XML
■ CSV
■ YAML
```
■ (HTML)
```
42
6
Data Formats
43
Lecture 06 - Data Formats
```
■ JSON, XML, YAML, TMOL, CSV, (TSV, WSV, etc.)
```
```
■ Structured vs unstructured (and semi-structured)
```
– Structured: CSV, XLSX*
– Less structured: JSON, YAML, TOML, XML
■ Plaintext - Not compressed
44
Lecture 06 - Data Formats
JSON
```
{
```
"firstName": "Paul",
"lastName": "Knutson",
```
"pet": null, // :(
```
"age": 25,
"education": [
"B.S. in Computer Engineering",
"M.S. in Computer and Data Science"
],
```
"computers": {
```
"laptop": "MacOS",
"desktop": "Windows 11",
"server": "Proxmox",
"phone": "iOS",
"tiktokphone": "Android"
```
}
```
```
} 45
```
Lecture 06 - Data Formats
YAML
---
```
firstName: Paul
```
```
lastName: Knutson
```
```
pet: # :(
```
```
age: 25
```
```
education:
```
- B.S. in Computer Engineering
- M.S. in Computer and Data Science
```
computers:
```
```
laptop: MacOS
```
```
desktop: Windows 11
```
```
server: Proxmox
```
```
phone: iOS
```
```
tiktokphone: Android
```
46
Lecture 06 - Data Formats
TOML
```
firstName = "Paul"
```
```
lastName = "Knutson"
```
```
age = 25
```
```
education = [
```
"B.S. in Computer Engineering",
"M.S. in Computer and Data Science"
]
[computers]
```
laptop = "MacOS"
```
```
desktop = "Windows 11"
```
```
server = "Proxmox"
```
```
phone = "iOS"
```
```
tiktokphone = "Android"
```
47
Lecture 06 - Data Formats
XML
<?xml version="1.0" encoding="UTF-8" ?>
<firstName>Paul</firstName>
<lastName>Knutson</lastName>
<pet />
<age>25</age>
<education>B.S. in Computer Engineering</education>
<education>M.S. in Computer and Data Science</education>
<computers>
<laptop>MacOS</laptop>
<desktop>Windows 11</desktop>
<server>Proxmox</server>
<phone>iOS</phone>
<tiktokphone>Android</tiktokphone>
</computers>
48
Lecture 06 - Data Formats
CSV
■ Importantly, many of my _SV files will include a space after the separator. This is
technically not correct, though most systems support it, and it makes the file more
readable. Bad habit, except sometimes.
firstName, lastName, pet, age, education, laptop, desktop, server, phone
Paul, Knutson, null, 25, "B.S. in Computer Engineering M.S. in Computer and Data Science", MacOS, "Windows 11",
Proxmox, "iOS and Android"
49
Lecture 06 - Data Formats
```
_SV: TSV, WSL, custom CSV
```
firstNamelastName pet age education laptop desktop server
Paul Knutson null 25 "B.S. …" MacOS "Windows 11" Proxmox
firstNamelastName pet age education laptop desktop server
Paul Knutson null 25 "B.S. …" MacOS "Windows 11" Proxmox
```
# sep=;
```
```
firstName; lastName; pet; age
```
```
Paul; Knutson; null; 25
```
```
Barack; Obama; Bo; 55
```
# sep=|
firstName|lastName|pet|age
Paul|Knutson|null|25
Barack|Obama|Bo|55
50
Lecture 06 - Data Formats
■ Anything you want! The world is yours! :D But the less custom, the more portable,
and the easier it will be for others to use your custom file format structure
■ Markdown table
■ HTML table
```
■ Single-line table (whitespace independent)
```
| firstName | lastName | pet | age |
| --------- | -------- | ---- | ---:|
| Paul | Knutson | null | 25 |
| Barack | Obama | Bo | 55 | a,b|1,2|3,4
51
Lecture 06 - Data Formats
Use cases
52
Store data sets Sensor data, DB data, structured data CSV, _SV, JSON
```
Send data (APIs) REST APIs, HTTP methods JSON, XML
```
Config files Infrastructure as Code, test config files YAML, JSON, XML
7
Web and HTTP
53
Lecture 07 - Web Services and HTTP
■ SOAP
– Simple Object Access Protocol
– Uses XML
■ RESTful
– Representation State Transfer
– Generally uses JSON, but can use any
– Client-server architectural style
– Communication is stateless
– High support for caching
– Uniform and well-defined interface
```
– Layered (hierarchical) structure
```
– “Web service is a software system designed
to support interoperable machine-to-
machine interaction over a network”.54
Lecture 07 - Web Services and HTTP
55
Lecture 07 - Web Services and HTTP
56575859
60
61
Lecture 07 - Web Services and HTTP
HTTP
■ Hypertext Transfer Protocol
■ TCP/IP
■ Used with most API systems
■ Methods:
– GET
– POST
– PUT
– DELETE
```
– and more (CRUD)
```
■ HTTP servers: Django, Gunicorn, Apache, ++
GET / HTTP/1.1
Keep-Alive: 300
```
Connection: keep-alive
```
```
Host: www.ntnu.no
```
```
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.1.12)Gecko/20100824 Firefox/3.5.12
```
```
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
```
```
Accept-Language: ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3
```
Accept-Encoding: gzip,deflate
```
Accept-Charset: windows-1251,utf-8;q=0.7,*;q=0.7
```
The HTTP method. Here the client
```
(web browser) is trying to GET some
```
information from the server
```
(www.ntnu.no).
```
The path In this example the
path points to the root of the
```
host (just /)
```
REQUES
T LINE
The request headers Since the request
does not have entity it only contains
general and request specific headers.
62
8
More about REST
63
Lecture 08 - More about REST
1. Figure out the data set
2. Split the data set into resources
3. Name the resources with URIs
4. Expose a subset of the uniform interface
5. Design the representation(s) accepted from the client
6. Design the representation(s) served to the client
7. Integrate this resource into existing resources, using hypermedia links and forms
8. Consider the typical course of events: What’s supposed to happen?
9. Consider error conditions: What might go wrong?
64
Lecture 08 - More about REST
65
Lecture 08 - More about REST
• Get all messages from the Sports category
– HTTP Method: GET
– URI: http://forum.example.com/Category/Sports
– Returns:
• On success: 200 OK + XML message body
• On error: 401 Unauthorized or 404 Not found
Successful HTTP response envelope
Request HTTP envelope
GET Category/Sports/ HTTP/1.1
```
Host: forum.example.com
```
```
Accept: text/xml
```
Accept-Encoding: gzip,deflate
Accept-Charset: windows-
```
1251,utf-8;q=0.7,*;q=0.7
```
HTTP/1.1 200 OK
```
Date: Sun 12 Sep 2010 11:30:12 GMT
```
Transfer-Encoding: chunked
```
Content-Type: text/xml;
```
```
Content-Length: length;
```
<?xml version="1.0" encoding="UTF-8"?>
<msg:Thread>
<msg:Message messageID="msg-3">
<msg:Registered userID="user-7">
<user:Nickname>HockeyFan</user:Nickname>
<user:Avatar file="avatar_7.jpg"/>
</msg:Registered>
<msg:Title>Edmonton's goalie</msg:Title>
<msg:Body>Does anyone know where Jussi...
```
(...)
```
</msg:Message>
```
(…)
```
<msg:Thread>
66
Lecture 08 - More about REST
WADL WSDL
Web Application Description Language Web Services Description Language
Made for REST Made for SOAP
Simpler More complex, but more flexible
Lightweight and easy to understand and write
compared to WSDL
More difficult to read and understand
WADL and WSDL are a bit like UML for data resources and describes how the data should be structured.
67
Lecture 08 - More about REST
68
<!-- Example -->
<lastname>Refsnes</lastname>
<age>36</age>
<dateborn>1970-03-27</dateborn>
<!-- Schema -->
<xs:element name="lastname" type="xs:string"/>
<xs:element name="age" type="xs:integer"/>
<xs:element name="dateborn" type="xs:date"/>
XML Schema
LECTURE
08 - MORE
ABOUT
REST
69
8.5 + 12.5
Testing
70
Lecture 08.5 + 12.5 - Testing
■ Unit testing, integration testing, API testing
– Unit: Small components
– Integration: Multiple components together
– API: Testing endpoints
– Stress testing: E.g., testing how much data an API can accept
■ Testing expected and unexpected
■ Type hinting, style guides, multi-env testing, GitHub Actions, etc.
71
9
CLI basics
72
10
Data Considerations
74
Lecture 10 - Data Considerations
Data characteristics
1. Physical characteristics
2. Performance requirements
3. Volatility
4. Volume
5. Regulatory requirements
6. Retention period
75
LECTURE 10 - DATA CONSIDERATIONS
76
Lecture 10 - Data Considerations
Relational DB or NoSQL DB?
Advantages of RDB
```
■ Great for online transaction processing (OLTP) activities.
```
■ Superior security features and a powerful querying engine.
Disadvantages
■ When data gets big, RDB just cannot perform fast enough.
77
Lecture 10 - Data Considerations
NoSQL
■ Similar to JSON structures or folder structures. Simple non-relational structures.
■ Much faster when retrieving close data.
■ Often less practical for complex queries.
■ Efficiency depends on what data you get and how it is structured. Examples:
– Get all phone numbers / check if phone number exists in your database.
```
– Get all data for about a specific post (data, title, text, user, likes, etc.).
```
78
10
Data Replications
79
LECTURE 10 -
DATA
REPLICATIONS
80
Lecture 10 - Data Replications
■ Permanent replicas
– Few replicas, statically configured
– Mirroring using mirror sites geographically spread across internet
```
■ Server-initiated replicas (push caches)
```
```
■ Client-initiated replicas (client caches)
```
81
Lecture 10 -
Data
Replications
■ Keep track of access counts per file, aggregated by considering server closest to
requesting clients
■ Number of accesses drops below threshold D ⇒ drop file
■ Number of accesses exceeds threshold R ⇒ replicate file
■ Number of accesses between D and R ⇒ migrate file
82
Lecture 10 - Data Replications
83
Lecture 10 - Data Replications
Push-based
■ Updates are propagated to other replicas even without their request
■ Often used between permanent and server-initiated replicas
```
■ When high degree of consistency (identical replicas) is required
```
■ Efficient when read-to-update ratio is high
Pull-based
■ Often used by client caches
■ Polls server to see if update is needed
■ Efficient when read-to-update ratio is relatively low
Hybrid form
■ Server pushed updated to client for a specified time
84
Lecture 10 - Data Replications
```
data = [
```
```
{
```
"request": "GET /contacts/137",
```
"return-data": "{\"name\": \"Obama\"}",
```
"counter": 100,
"request-time": "2023-05-08 18:49"
```
},
```
. . .
]
85
Lecture 10 - Data Replications
```
def get_value_from_main_API(request):
```
```
# request.get(URI request) and so on
```
```
return {"nothing": "nothing"}
```
```
def get_value_from_cache(request):
```
global data
for value in data:
if value["request"] == request:
return value
return None
86
Lecture 10 - Data Replications
```
def get_value(request):
```
global data
```
value = get_value_from_cache(request)
```
if value is None:
# Forward request to main API
```
value = get_value_from_main_API(request)
```
```
data.append({
```
"request": request,
"return-data": value,
"counter”: 100,
```
"request-time": time.time()
```
```
})
```
. . .
. . .
```
else:
```
# Using counter
value["counter"] -= 1
if value["request"] <= 0:
# But copy first?
del value
# Using request-time
```
if value["request-time"] > time.time() -
```
10_000:
del value
return value
87
Lecture 10 - Data Replications
Data store
Primary server
for item x
Client Client
Backup server
W1. Write request
W2. Forward request to primary
W3. Tell backups to update
W4. Acknowledge update
W5. Acknowledge write completed
W2
W3 W3
W3
W4 W4
W4
W1 W5
R1. Read request
R2. Response to read
R1 R2
88
11
Docker
91
Lecture 11 - Docker
■ Basically a VM lite
■ Isolates your system/program from the global environment
– And makes your system runnable on most systems with no hassle
– Make code locally, push to server … will it run?
■ You can also download and run containers like modules
92
Lecture 11 - Docker
9394
Lecture 11 - Docker
■ Docker client + server and the registry
```
■ Docker images (container template)
```
```
■ Docker containers (“VM”)
```
■ Docker file: Setup file
■ Volumes
■ Networks
95
Lecture 11 - Docker
96
97
Lecture 11 -
Docker
98
Lecture 11 - Docker
■ Example of a Dockerfile
FROM node:19
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV PORT=8080
EXPOSE 8080
RUN echo "The ARG variable value is $PORT"
CMD ["npm", "start"] 99
12
Docker Compose
100
Lecture 12 - Docker Compose
■ Commands
docker ps
docker images
docker run ...
docker rm/rmi ...
docker-compose up
docker-compose up --build
docker-compose down
101
Lecture 12 - Docker Compose
```
services:
```
```
minecraft:
```
```
image: itzg/minecraft-server
```
```
ports:
```
- "25565:25565"
```
environment:
```
```
EULA: "TRUE"
```
```
deploy:
```
```
resources:
```
```
limits:
```
```
memory: 1.5G
```
```
volumes:
```
- "~/minecraft_data:/data"
102
Lecture 12 - Docker
Compose
■ Docker volumes: Bind mount vs Volume
103
Lecture 12 - Docker Compose
■ docker run vs docker-compose
– Run launches single container from image
```
– Compose launches single or multiple image(s) at once, including networking
```
– Uses YAML file instead of multi-parameter commands
docker run --rm -p 5001:8080 --restart always catsymptote/dockerdemo
```
name: app
```
```
services:
```
```
dockerdemo:
```
```
ports:
```
- 5001:8080
```
restart: always
```
```
image: catsymptote/dockerdemo 104
```
Lecture 12 - Docker
Compose
■ Scaling: Split large number of users, calls
or processes onto multiple smaller nodes
– Vertical vs horizontal scaling: Bigger
computers vs more computers
– Load balancing
– Docker scale, Docker swarm and
```
Kubernetes (k8s)
```
105
Lecture 12 -
Docker Compose
```
■ Kubernetes (k8s)
```
106
Lecture 12 -
Docker Compose
■ Dashboards, like Grafana or
```
Horizon (OpenStack)
```
■ Logging
107108
13
Cloud Extras
109
Lecture 13 - Cloud Extras
■ git: CLI vs GUI, branches, remotes, authentication
■ Security: Cryptography, encryption, checksums, certificates, passwords
– Access: Software and hardware
```
– SSH and SSH keys (asymmetric cryptography)
```
```
■ Files and formats: Plaintext vs binary, compression and conversion (lossy and
```
```
lossless)
```
■ Hardware infrastructure: Storage, transfer, processing, memory
110
Lecture 13 - Cloud Extras
■ Cost models: Usage, periodic, permanent
– CPU time, RAM amount+time, storage amount, transfer/bandwidth
– Domains
– API costs: Per request, free requests
■ Software/hardware costs
– Duration of software and hardware
– Investment in future-proofing
111
Lecture 13 - Cloud Extras
■ Caches: When to cache, cache location, personal cache
```
■ Load balancing: When it can make sense (symmetric)
```
■ CLI/shell: Basic commands, moving around in the folders, basic knowledge of
Linux/Unix directory structure
112
Lecture 13 - Cloud Extras
Files and formats
■ Plaintext vs binary
■ Compression
■ Images and video
– Bitmap vs vector
■ Export files vs work files
■ Conversion and information loss
■ ‘
113
Lecture 13 -
Cloud Extras
115
Lecture 13 - Cloud
Extras
■ git
116
Lecture 13 - Cloud Extras
117
LABS
118
Lab 1 – Python install
■ Set up Python and VS Code
120
Lab 2 – Python
basics
■ Python basics
■ Load and print CSV data
# Load text
```
with open('2-Python/contacts.csv') as f:
```
```
text = f.read()
```
# Split text into list of lines
```
lines = text.split('\n')
```
# for each line
for line in lines:
# Alternative solution?
```
# new_line = line.replace(';', ' ')
```
# Split line into individual items
```
items = line.split(';')
```
# For each line
for item in items:
```
# Print item (13 col width)
```
```
print(f'{item:13}', end='')
```
# Add new-line before next line
```
print() 121
```
Lab 3 –
Python less
basics
■ Parsing of vCard files
■ Saving to JSON
# Read text from file.
```
with open('04-Python-Less-Basic/sample-1.vcf') as f:
```
```
text = f.read()
```
# Split text by line.
```
lines = text.split('\n')
```
# Create empty dictionary/JSON.
```
contact = {}
```
# Loop through lines.
for line in lines:
# If line has no colon, skip this line.
if ':' not in line:
continue
# Split line on colon, and add to dictionary.
```
key, value = line.split(':')
```
contact[key] = value
# Print as JSON.
import json
```
print(json.dumps(contact, indent=4)) 122
```
Lab 4 – Python APIs
■ Made a script using a public API
■ Made a simple Python API using FastAPI
■ Made another script which used this API
from fastapi import FastAPI
```
app = FastAPI()
```
```
@app.get('/')
```
```
def read_root():
```
```
return {'Hello': 'World! :D'}
```
```
@app.get('/items/{item_id}')
```
```
def read_item(item_id: int, q: str | None = None):
```
```
return {'item_id': item_id, 'q': q} 123
```
Lab 5 – Render
■ Set up FastAPI example on Render
124
Lab 6 – Data formats
■ Structuring data in
different formats
---
```
name: Proxmox server
```
```
computers:
```
- ComputerNum: '01'
```
OS: Debian
```
```
Hosting: TrueNAS
```
- ComputerNum: '02'
```
OS: Ubuntu
```
```
Hosting: media server
```
```
Submodules: []
```
- ComputerNum: '03'
```
OS: Ubuntu
```
```
Hosting: Portainer
```
```
Submodules:
```
- Wireguard VPN
- DuckDNS
- MongoDB
- ComputerNum: '04'
```
OS: Windows 11
```
```
Hosting: backup server
```
```
{
```
"name": "Proxmox server",
"computers": [
```
{
```
"ComputerNum": "01",
"OS": "Debian",
"Hosting": "TrueNAS"
```
},
```
```
{
```
"ComputerNum": "02",
"OS": "Ubuntu",
"Hosting": "media server",
"Submodules": []
```
},
```
```
{
```
"ComputerNum": "03",
"OS": "Ubuntu",
"Hosting": "Portainer",
"Submodules": [
"Wireguard VPN",
"DuckDNS",
"MongoDB"
]
```
},
```
```
{
```
"ComputerNum": "04",
"OS": "Windows 11",
"Hosting": "backup server"
```
}
```
]
```
}
```
ComputerNum, OS, Hosting
01, Linux Debian, TrueNAS
02, Linux Ubuntu, media serv.
03, Linux Ubuntu, Portainer
04, Windows 11, backup serv. 125
Lab 7 – API cache
■ Set up two APIs on Render
– A main node
```
– A passthrough node (almost a cache)
```
127
Lab 8 – Testing
■ Set up loads of testing config files:
– pyproject.toml, requirements.txt, setup.cfg, setup.py, tox.ini, .github/…/….yml
– These allowed us to run automatic tests locally and as GitHub Actions, as well
```
as installing our code as a local Python module (callable using `python -m
```
modulename`
– Most of these config files should be copy-pasted from previous projects, and
modified to fit our project
```
■ Some basics of unit testing, type checking and style guides (pytest, mypy, flake8)
```
128
Lab 9 – Caching
■ Used existing external currency API and added a local cache to it
■ Allowed the API to check our local cache before spamming the external API
129
Lab 11 – Docker
■ Set up a simple JS server using Docker
■ Dockerfile, package.json,
.dockerignore, index.js
■ Also did some extra unit testing setup
FROM node:19
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV PORT=8080
EXPOSE 8080
RUN echo "The ARG variable value is $PORT"
CMD ["npm", "start"]
133
Lab 12 – Docker compose
```
■ Used docker-compose to launch bigger project (web API with a MongoDB) using a
```
```
single command (docker-compose up)
```
134
TAKK FOR I ÅR :D
136