# **Web services and HTTP**


## **URI**


- [According to W3C (http://www.w3.org/TR/ws-arch):](http://www.w3.org/TR/ws-arch))

  - _“Web service is a software system designed to support interoperable_ _**machine-to-**_

_**machine interaction**_ _over a network”._


It’s basically a web page for machines.


Separate systems with clearly defined interfaces

   - Which **functionality** they perform

   - Which **data format** the operate

Application independent

   - No need to rebuild
every system from
scratch


Provider


 - The server in the server-client system


 - Also used to refer to the org.
hosting the service. E.g., Google.


Consumer


 - The client

 - Sends requests messages (for data and such)


- ”Big Web services” (SOAP)

- RESTful


**S** imple **O** bject **A** ccess **P** rotocol

- Format/language for sending and receiving messages

- Uses XML (or anything, really)

- Classical SOA (Service-Oriented Architecture)


More about SOAP:

https://www.w3schools.com/XML/xml_soap.asp


**Re** presentation **S** tate **T** ransfer

- Architectural style


**Re** presentation

- REST is resource-oriented

- Any information which can be named is a resource

- Each resource can have several representations


**S** tate

- Each resource has a state (which is different from the state of the application)


**T** ransfer

- The state can be transferred (and retrieved/modified)


- Client-server architectural style

- Communication is stateless

- Caching

- Uniform and well-defined interface

- Layered (hierarchical) structure


REST is generally run on HTTP


- Provides the client-server communication


- Provides interfaces with the HTTP methods

- Is stateless


REST concepts can be applied to other protocols


- E.g. Stateless interaction with an FTP site


**H** yper **t** ext **T** ransfer **P** rotocol


- _“an_ _**application-level protocol**_ _for distributed, collaborative, hypermedia information_
_systems”_


- Usually works on TCP/IP

- The most used protocol in WWW


- Used for most API systems

- Allows for bidirectional transfer of resources between client and server


|Col1|The request headers Since the request<br>does not have entity, it only contains<br>general and request specific headers.|
|---|---|
|<br>|<br>|


CRUD


- GET

- POST

- PUT

- DELETE


- PATCH


- HEAD

- OPTIONS


Apache httpd, nginx

ISS (Microsoft web server)

Python: Django, Gunicorn, Uvicorn (+Flask)

Java: Glassfish


Python: httplib2 or http.server

JS/Node.JS: http module

Java: HttpClient

C#: System.Web.HTTPWebRequest

C and PHP: libcurl


- Use the (built-in) Python module http.server to launch a simple
http server locally.

- This should allow you to view your folder structure.


- Relational, document, NoSQL, key-value, graph


Set up FastAPI (from a previous lab?) on Render.

See MD-file on GitLab


- Set up GitHub Education (or whatever it’s called) so you get
access to GitHub Co-pilot (Chat).


