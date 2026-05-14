# **Data Formats**


## **Happy Valentine’s**








## **Data format**

#### • Storing and sending • Compression • Structured vs unstructured • Plaintext and serialization • Readability • Compatibility


## **Data formats**

#### • JSON • XML • CSV • TSV, WSV and other _SV • YAML • TOML • …


## **Structured and Unstructured**


###### **Structured**
#### • Data which follows a pre- defined structure. • Lower effort to use the data. • Quantitative.


###### **Unstructured**
#### • Data which does not. • Higher effort to use the data. • Qualitative.


## **Semi-structured data**

#### • Weak structure rules, which must include metadata


## **Structured and Unstructured**


###### **Structured**
#### • CSV • _SV • Xlsx (kind of) • RDB/SQL DBs


###### **Semi-structured**
#### • JSON • YAML • TOML • XML • NoSQL DBs


###### **Unstructured**
##### • Text • Images • Binary data • NoSQL DBs


## **Data formats – JSON**

{

"firstName": "Paul",
"lastName": "Knutson",
"pet": null, _// :(_
"age": 25,
"education": [

"B.S. in Computer Engineering",
"M.S. in Computer and Data Science"
],
"computers": {

"laptop": "MacOS",
"desktop": "Windows 11",
"server": "Proxmox",
"phone": "iOS",
"tiktokphone": "Android"
}
}


## **Data formats – YAML**

--firstName: Paul
lastName: Knutson
pet: _# :(_
age: 25
education:

            - B.S. in Computer Engineering

            - M.S. in Computer and Data Science
computers:

laptop: MacOS
desktop: Windows 11
server: Proxmox
phone: iOS
tiktokphone: Android


## **Data formats – TOML**

firstName = "Paul"
lastName = "Knutson"
age = 25
education = [
"B.S. in Computer Engineering",
"M.S. in Computer and Data Science"
]


[computers]
laptop = "MacOS"
desktop = "Windows 11"
server = "Proxmox"
phone = "iOS"
tiktokphone = "Android"


## **Data formats – XML**

<?xml _version_ ="1.0" _encoding_ ="UTF-8" ?>
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


## **Data formats – CSV**

firstName, lastName, **pet,** _age,_ education, laptop, desktop, **server, phone**
Paul, Knutson, **null,** _25,_ "B.S. in Computer Engineering, M.S. in Computer and …

… Data Science", MacOS, Windows 11, **Proxmox, "iOS and Android"**


## **Data formats – _SV**

firstName lastName pet age education laptop desktop server phone
Paul Knutson null 25 "B.S. in Computer Engineering, M.S. in Computer and Data Science" MacOS Windows 11 Proxmox
"iOS and Android"


firstName lastName pet   age   education …
Paul       Knutson   null   25    "B.S. in CE …"


# sep=;
firstName;lastName; **pet;** _age_
Paul;Knutson; **null;** _25_
Barack;Obama; **Bo;** _55_


## **Data formats – Use cases**

#### • Store data sets (json, csv, etc.) - E.g., sensor data, DB data • Send data (json, etc. for APIs) - E.g., REST APIs • Config files (json, yaml, toml) - E.g., Infrastructure as Code (IaC)


### **Use example** **GitHub Actions**



name: Tests


on:

- push

- pull_request


jobs:

test:

runs-on: ${{ matrix.os }}
strategy:

matrix:

os: [ubuntu-latest, windows-latest, macos-12]
python-version: ['3.7', '3.8', '3.9', '3.10']


steps:

   - uses: actions/checkout@v2

   - name: Set up Python ${{ matrix.python-version }}

uses: actions with:/setup-python@v2

python-version: ${{ matrix.python-version }}


   - name: Install dependecies

run: |

python -m pip install --upgrade pip
pip install tox tox-gh-actions

   - name: Test with tox

run: tox


### **Use example** **IaC config**



{

"name": "Main-Server",
"VMs": [

{

"name": "Application-VM",
"OS": "Debian",
"cores": 2,
"RAM": 2,
"storage": 100
},
{

"name": "Processing-VM",
"OS": "Debian",
"cores": 4,
"RAM": 4,
"storage": 100
},
{

"name": "Database-VM",
"OS": "Ubuntu",
"cores": 2,
"RAM": 8,
"storage": 100
},


]
}


### **Use example** **IaC config**



name,OS,cores, _RAM,_ storage
Application-VM,Debian,2, _2,_ 100
Processing-VM,Debian,4, _4,_ 100
Database-VM,Ubuntu,2, _8,_ 100


## **Generic IaC example**

#### • Copy template VM (VirtualBox file) • Rename • Modify settings (cores, RAM, etc.) • Launch • Automatically do some setup within VM? Using SSH?

cp Ubuntu-Template Application-VM
virtualbox --modifyVM Application-VM name:Application-VM os:Debian cores:2 RAM:2 storage:100
virtualbox --launchVM Application-VM


## **Online converters exist**

#### • For example:
###### • json2yaml.com • https://jsonformatter.org/json-to-xml

#### • Use them! (But not yet.)


## **Data formats – Group work**

###### We have two sets of data. Store the data as all relevant/fitting formats (from prev. pages): JSON, YAML, TOML, XML, CSV/_SV


##### • Proxmox server

   - # ComputerNum, OS, Hosting

   - 01, Linux Debian, TrueNAS

   - 02, Linux Ubuntu, media serv.

   - 03, Linux Ubuntu, Portainer

      - Wireguard VPN

      - DuckDNS

      - MongoDB

   - 04, Windows 11, backup serv.


##### • Students # Grades

   - Erna, Solberg

      - Maths, C

      - Programming, D

   - Gandalf, The Grey

      - Maths, E

      - Programming, B

   - Albert, Einstein

      - Maths, A

      - Programming, F


## **Optional homework**

#### Set up GitHub Education (or whatever it’s called) so you get access to GitHub Co-Pilot (Chat).


