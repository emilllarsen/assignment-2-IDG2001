### **A G E N DA**


- XML schema


- RESTful web service design


- WADL and WSDL




### **X M L S C H E M A**

[•](https://www.w3schools.com/xml/schema_intro.asp) [XML Schema Tutorial (w3schools.com)](https://www.w3schools.com/xml/schema_intro.asp)


- Common types

  - xs:string

  - xs:decimal

  - xs:integer

  - xs:boolean

  - xs:date

  - xs:time




### **X M L S C H E M A V S X M L**


- Example and its schema


_<!-- Example -->_
<lastname>Refsnes</lastname>
<age>36</age>
<dateborn>1970-03-27</dateborn>


_<!-- Schema -->_
<xs:element name="lastname" type="xs:string"/>
<xs:element name="age" type="xs:integer"/>
<xs:element name="dateborn" type="xs:date"/>




### **X M L S C H E M A E X A M P L E**




- As schema



<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">


<xs:element name="note">
<xs:complexType>
<xs:sequence>
<xs:element name="to" type="xs:string"/>
<xs:element name="from" type="xs:string"/>
<xs:element name="heading" type="xs:string"/>
<xs:element name="body" type="xs:string"/>
</xs:sequence>
</xs:complexType>
</xs:element>


</xs:schema>




### **X M L S C H E M A E X A M P L E A S X M L**


- As XML


<?xml version="1.0" encoding="utf-8"?>
_<!-- Created with Liquid Technologies Online Tools 1.0 (https://www.liquid-_
_technologies.com) -->_
<note xsi:noNamespaceSchemaLocation="schema.xsd"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<to>string</to>
<from>string</from>
<heading>string</heading>
<body>string</body>
</note>




# **R E S T F U L W S D E S I G N S T E P S**

A n d s - m e A P I e x a m p l e s




### **Y E T A N O T H E R S I M P L E A P I**

@app.GET("/c2f")
def c2f( _value_ : float):
_return_ {"c": _value_                                - 9/5 + 32}


@app.GET("/f2c")
def f2c( _value_ : float):
_return_ {"f": ( _value_                                - 32) * 5/9}




### **S I M P L E R P C - L I K E A P I ( AT H O M E )**

@app.GET("/")
def update_server():
_import_ subprocess
subprocess.run(["sudo", "apt", "update", "&", "sudo", "apt", "upgrade", "-y"])




### **S I M P L E Q U E RY / G R A P H Q L ( F R O M** **T E M U )**

@app.GET("/")
def search_db( _query_ ):
'''query = {"query": "SELECT * FROM TABLE users"}'''
_return_ ... _# Run database query_




### **W H Y E V E N H AV E R U L E S ?**

_# Do-everything-API-endpoint_
@app.POST("/")
def perform_query( _body_ ):
_# {"command": "query", "message": "SELECT * FROM ALL TABLES"}_


_if_ _body_ ["command"] == "query":
_query_ = _body_ ["message"]
_# Query the database ..._


_elif_ _body_ ["command"] == "cmd":
_import_ subprocess
subprocess.run( _body_ ["message"])




### **R E S T F U L**



REST is about data – and its representations




### **R E S T F U L W S D E S I G N S T E P S**

1. Figure out the data set


2. Split the data set into resources


3. Name the resources with URIs


4. Expose a subset of the uniform interface


5. Design the representation(s) accepted from the client


6. Design the representation(s) served to the client


7. Integrate this resource into existing resources, using hypermedia links and forms


8. Consider the typical course of events: what’s supposed to happen?


9. Consider error conditions: what might go wrong?




### **1 . F I G U R E O U T T H E DATA S E T**


- Define what to expose (concepts)


- Describe their relationships




### **1 . F O R U M E X A M P L E**

- The forum application permits users of the forum to publish new messages.


- Users can post a message in different categories, or can have answer messages
from other users.


- Every user has a public profile and a private profile that is shown only to their
friends. Every user can check the public profile or other users.


- Users can also check which were the last messages they posted/commented.


- Users can also search messages in the forum using several criteria: keywords, user,
popularity, date published/commented...


### **2 . S P L I T T H E DATA I N T O R E S O U RC E S**

RESTful Web services expose 3 kinds of resources:

- Predefined **one-off** resources for especially important aspects of the application.

   - E.g.: Repository for other resources

   - Those resources cannot be deleted or modified the state

- A resource for every **object** exposed through the service.

   - One service may expose many kinds of objects, each with its own resource set.

   - Most services expose a large or infinite number of these resources.

- Resources representing the results of **algorithms** applied to the data set.

   - This includes collection resources, which are usually the results of queries


### **2 . S P L I T T H E DATA I N T O R E S O U RC E S**

At this step, you should define the hierarchy for the resources


- Can be tricky, but think of the result of the action. E.g. list of forum messages


Hints:


- Define all possible types of resources the web service is intended to expose and
how these types of resources fit in the hierarchy.


- Take into account the platform you are going to use in this step. Some platforms
make it easier to create resources in one way, others in another.


### **S T E P 3 - N A M E T H E R E S O U R C E S W I T H** **U R I S**

- You must name each resource defined in the previous step

- Each resource type must have a URI pattern

- In a resource-oriented service the URI contains all the scoping information.

- There are three rules for URI design:

1. Use path variables to encode hierarchy: **/parent/child**
2. Use punctuation characters in path variables when there is no hierarchical relation :


 - **/parent/child1;child2**

   - Use commas when the order of the scoping is important

   - Use semicolon in other case


3. Use query variables to imply inputs into an algorithm, for example: **/search?q=category**

- Forum Examples:


[–](http://forum.example.com/Users/user1) **[http://forum.example.com/Users/user1](http://forum.example.com/Users/user1)**

[–](http://forum.example.com/Categories/Science) **[http://forum.example.com/Categories/Science](http://forum.example.com/Categories/Science)**

[–](http://forum.example.com/messages/message1;message2) **[http://forum.example.com/messages/message1;message2](http://forum.example.com/messages/message1;message2)**

[–](http://forum.example.com/Users/user1/history?last=5) **[http://forum.example.com/Users/user1/history?last=5](http://forum.example.com/Users/user1/history?last=5)**

          - Returns a list of the last 5 messages posted by user1.


### **S T E P 4 - E X P O S E A S U B S E T O F T H E** **U N I F O R M I N T E R FA C E**

- Explain what happens to each resource when it is exposed to any of the methods of the uniform interface.

  - A resource does not have to expose all the methods.

  - If your resource is read-only, then three method implementations is enough (GET, HEAD and/or OPTIONS).

  - If your resource can be created or modified you need to implement PUT, POST and/or DELETE

- Avoid creating your own method (by overloading POST)

  - If you think you need an extra method, change the verb by a noun and transform it into a resource.

  - Example: If you think you need a method named publish just create a resource named publication. Use the uniform
interfaces to modify it.


### **S T E P 4 - E X P O S E A S U B S E T O F T H E** **U N I F O R M I N T E R FA C E**

Forum Examples:

**Get all messages from the Sports category**

   - **GET** **[http://forum.example.com/Category/Sports](http://forum.example.com/Category/Sports)**


**Create a new User. Users have a unique nickname defined during registration**

  - **PUT** **[http://forum.example.com/Users/nicky](http://forum.example.com/Users/nicky)**

    - User details in the HTTP request body.


**Post the message into Science category**

  - **[POST http://forum.example.com/Category/Science/Messages](http://forum.example.com/Category/Science/Messages)**

        - message content and posting user details are in the message body


**Delete the message**

  - **DELETE** **[http://forum.example.com/Category/Computers/Messages/msg-4](http://forum.example.com/Category/Computers/Messages/msg-4)**


#### **S T E P S 5 & 6 - D E S I G N R E P R E S E N T A T I O N S** **A C C E P T E D F R O M T H E C L I E N T / S E R V E D T O** **T H E C L I E N T**

Assign to each resource a representation or set of representations

  - The **representation** is the format in which we transfer the resource state between client and server.


  - The format should allow links to other application and resource states.


  - The same resource could have different representations

        - The server should understand any representation sent by the client.

        - The server should send to the client a representation that it can understand.

        - The client asks for a specific format in the URI:


               - » E.g.: **[http://forum.example.com/users/user_1.xml](http://forum.example.com/users/user_1.xml)**


The resource representation is encapsulated in the HTTP request/response message

  - The HTTP body contains the representation


  - The HTTP entity headers contains metadata related to the representation


  - Other headers can be used for other purposes such as caching, authorization...


#### **S T E P S 5 & 6 - D E S I G N R E P R E S E N T A T I O N S** **A C C E P T E D F R O M T H E C L I E N T / S E R V E D T O** **T H E C L I E N T**

When defining the representation we need to set:

   - What resource metadata it is going to be sent in the headers


   - The format of the HTTP body:


          - Plain strings


          - JSON, XML


          - HTML,XHTML


          - Atom, RSS


          - SVG


          - JPG, GIF


          - MP3


          - …

   - NOTE: HTTP headers “Content-Type” and “Content-Length” tell the other partner the format of the HTTP body and its length in decimal number of OCTETs

          - A list of mime types can be found in RFC2045 and RFC2046


When the representation is not a markup language (e.g. image, audio…), connecting to other resources is impossible.


   - You should always encapsulate this resource into other resource that allows connectedness


#### **S T E P S 5 & 6 - D E S I G N R E P R E S E N T A T I O N S** **A C C E P T E D F R O M T H E C L I E N T / S E R V E D T O** **T H E C L I E N T**

Plain string

  - The specifically created data interchange protocol. Both client and server must know how to interpret it.

  - Forum Example **:**




     - “CATEGORY: CATEGORYID=cat-1, NAME=Science, DESCRIPTION=Physics, chemistry, mathematics and other areas of science.”
JSON




  - Lightweight text-based open standard designed for data interchange.

  - Forum Example:

   - {“CategoryID”:”cat-1”, “Name”: “Science”, ”Description”: “Physics, chemistry, mathematics and other areas of science.”}
XML




- The representation format should be agreed between client and server, hence both of them would be



able to process the data correctly.

  - Use XML Schema, DTD or Schematron for that purpose.
XHTML




- XML which includes formatting instructions.

- This one which fits better in ROA architecture.

- Allows creating links between resources and forms to receive data from the client.




### **S T E P 7 - L I N K R E S O U RC E S T O E AC H** **O T H E R**

- Each resource must have links to other resources/states.

  - A diagram for each resource type presenting all possible links could help in the design.

- If using XHTML:

  - Use <a> to link to other resource

  - Use <form> when:

      - You want to include in the URI a query string

      - Represent infinite URIs that follow a certain pattern.

- In XML

  - Use Xlink and XPointer to link to other resources

      - Alternative, use the atom:link element

  - Use URI template to include query string and represent infinite URI.


### **S T E P 8 - D E F I N E T H E C O U R S E O F** **E V E N T S**

`o` The response includes a response code indicating if the request was processed

successfully in the server or not.

`o` Response code + headers indicating success:

|200 OK|No headers|Successful request|
|---|---|---|
|304 Not Modified|No headers|The client must get the resource from the cache|



   - DELETE


   - POST and PUT


|201 Created|Location|Successful creation. Location header indicates the<br>URI of the resouce|
|---|---|---|
|200 OK|No headers|The resource existed and has been modified. The<br>Body could contain the new resource|
|301 Moved<br>permanently|Location|The data sent makes the resource changes the URI|


### **S T E P 9 - D E F I N E P O S S I B L E E R R O R S**


   - Define when and how a request could fail.

   - GET and DELETE

|404 Not Found|No headers|Resource is not found. HTTP body message could<br>contain an error message|
|---|---|---|
|303 See Other|Location|The resource is not found. Location header<br>provides a related resource|
|400 Bad Request|No header|The URI contains some impossible fields or<br>parameters|



   - PUT and POST


|415 Unsopported Media<br>Type|No headers|The representation format is not supported in the<br>server|
|---|---|---|
|409 Conflict|No header|The representation tries to change the state of the<br>resource to an impossible one|
|400 Bad Request|No header|The resource representation contains invalid value|


### **F O R U M E X A M P L E - G E T**


- Get all messages from the Sports category

   - **HTTP Method:** `GET`

   - **URI:** `[http://forum.example.com/Category/Sports](http://forum.example.com/Category/Sports)`

   - **Returns:**

          - On success: `200` `OK` + XML message body

          - On error: `401` `Unauthorized` or `404` `Not found`


**Successful HTTP response envelope**



**Request HTTP envelope**

```
GET Category/Sports/ HTTP/1.1
Host: forum.example.com
Accept: text/xml
Accept-Encoding: gzip,deflate
Accept-Charset: windows1251,utf-8;q=0.7,*;q=0.7

```

```
HTTP/1.1 200 OK
Date: Sun, 12 Sep 2010 11:30:12 GMT
Transfer-Encoding: chunked
Content-Type: text/xml;
Content-Length: length;

<?xml version="1.0" encoding="UTF-8"?>
<msg:Thread>
 <msg:Message messageID="msg-3">
  <msg:Registered userID="user-7">
   <user:Nickname>HockeyFan</user:Nickname>
   <user:Avatar file="avatar_7.jpg"/>
  </msg:Registered>
  <msg:Title>Edmonton's goalie</msg:Title>
  <msg:Body>Does anyone know where Jussi...
 (...)
 </msg:Message>
(…)
<msg:Thread>

```



### **F O R U M E X A M P L E - P O S T**


- Post the message into Science category

    - **HTTP Method:** POST

    - **URI:** [http://forum.example.com/Category/Science/Messages](http://forum.example.com/Category/Science/Messages)

    - **Request:** XML message body

    - **Returns:**

           - On success: 201 Created (Location header tells the URI of created message)

           - On error: 400 Bad Request or 409 Conflict


**Request HTTP envelope** **Successful** **HTTP response envelope**


```
POST Category/Science/Messages HTTP/1.1
Host: forum.example.com
Accept: text/xml
Accept-Encoding: gzip,deflate
Accept-Charset: windows-1251,utf8;q=0.7,*;q=0.7
Content-Type: text/xml;charset=utf-8
Content-Length: length

<?xml version="1.0" encoding="UTF-8"?>
<msg:Message messageID=“" replyTo="msg-1">
 <msg:Anonymous>Science guru</msg:Anonymous>
 <msg:Title>In case</msg:Title>
 <msg:Body>Just in case you can't …
(...)
</msg:Message>

```

```
HTTP/1.1 201 Created
Date: Tue, 19 Sep 2010 06:11:22 GMT
Content-Type: text/xml; charset=iso-8859-1
Content-Length: length
Location:
http://forum.example.com/Category/Science/Messages/msg-4

<?xml version="1.0" encoding="UTF-8"?>
<msg:Message messageID=“msg-4" replyTo="msg-1">
 <msg:Anonymous>Science guru</msg:Anonymous>
 <msg:Title>In case</msg:Title>
 <msg:Body>Just in case you can't ...
(...)
</msg:Message>

```

### **F O R U M E X A M P L E - D E L E T E**

Delete certain message

   - **HTTP Method:** DELETE

   - **URL:** [http://forum.example.com/Category/Science/Messages/msg-4](http://forum.example.com/Category/Science/Messages/msg-4)

   - **Returns:**

         - On success: 204 No Content

         - On error: 401 Unauthorized or 404 Not Found



**Request HTTP envelope**

```
DELETE
Category/Science/Messages/msg-4
HTTP/1.1
Host: forum.example.com
Accept: text/xml, text/html
Accept-Encoding: gzip,deflate
Accept-Charset: windows-1251,utf8;q=0.7,*;q=0.7
Keep-Alive: 300
Connection: keep-alive

```


**Error** **HTTP response**

```
HTTP/1.1 404 Not Found
Date: Tue, 19 Sep 2010 06:11:22 GMT
Content-Type: text/html; charset=iso-8859-1
Content-Length: length
Keep-Alive: timeout=15, max=96
Connection: Keep-Alive
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
 <head>
 <title>404 Not Found</title>
 </head>
 <body>
 <h1>Not Found</h1>
 <p>The requested message msg-4 was not found on this
server.</p>
 </body>
</html>

```

### **W E B S E R V I C E D E S C R I P T I O N**

How to make the clients aware of the functionality of our WS & exposed resources?


- With textual descriptions plus some data format definitions (e.g. XML Schema)


- With a **format** web service description (a contract), which specifies the service
interface, communication protocols and message details


  - Allows to build the tools for automatic generation of stubs and skeleton code
for WS clients and providers


  - Publishing, testing and configuration of WS


### **W E B S E R V I C E D E S C R I P T I O N**

Formal WS descriptions should include


- Service’s URL information


- Service’s communication mechanisms


- Service’s methods description, together with I/O information


- Message details




### **W E B S E R V I C E D E S C R I P T I O N**

There are two relevant strong formal description languages for REST WS:


- WSDL (2.0)


- WADL




### **WA D L V S W S D L**

WADL


- Made for REST


- Simpler


- Lightweight and easy to understand
and write compared to WSDL



WSDL


- Made for SOAP


- More complex, but more flexible


- More difficult to read and understand


### **WA D L**

- **Resources** is the container for the resources provided by the application.

- **Resource** element describes a set of resources, each identified by URI that follows
a common pattern.

- **Method** element describes the input to and output from an HTTP protocol method
that may be applied to a resource.

- **Param** element describes a parameterized component of its parent element.


### **W S D L**


- WSDL (Web Services Description Language) is the XML language which formally describes the Web service. WSDL 1.1 is the most widely
used protocol for SOAP Web Services description, however it doesn’t provide the good support for RESTful Web services. WSDL 2.0 was
designed with having REST in mind (provides **HTTP binding** ).

- WSDL description contains

   - Service’s URL information

   - Service’s communication mechanisms

   - Methods description (interface)

   - Message structure

- Some tools which work with WSDL 2.0

   - Woden, WSDL 2.0 processor

   - Axis2, Web service runtime engine capable of generating Java client and server stubs from WSDL 2.0 document


```
<wsdl:description xmlns:wsdl=“http://www.w3.org/ns/wsdl”>
  <wsdl:service/>
  <wsdl:types/>
  <wsdl:interface/>
  <wsdl:binding/>

</wsdl:description>

```

**Service** element associates an address for the Web service with a specific interface and binding.
**Binding** element defines how the client can
communicate with the service
**Types** elemenet contains all of the XML schema element and type definitions that describe Web service’s messages
**Interface** element defines the Web service’s
operations, including input, output, fault messages and the order in which they are passed


### **W S D L V S W A D L**

**Criteria** **WSDL 2.0**
**HTTP Binding**



**WADL**



Communication Transport protocol- HTTP
independent





HTTP response codes Only for faults For all operations


URI templates Yes Yes


Authentication support Yes No


For more details refer to “Definition Languages for RESTful Web Services: WADL vs. WSDL 2.0” by T.Takase et al.
and WADL and WSDL 2.0 specifications




