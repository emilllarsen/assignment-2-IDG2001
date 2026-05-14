Info

Question

Question title

Marks

Question type

IDG2001-V2025-2-KONT

Forside

Information or resources

Exam structure and info

Information or resources





Write

Question

Question title

Marks

Question type

1

2

3

4

5

6

Python

HTTP methods

OSI

Virtualization and containerization

Pros and cons of cloud

Plant detection app

10

10

10

10

20

40

Programming

Essay

Essay

Essay

Essay

Essay

1/10

IDG2001-V2025-2-KONT

 Forside

Examination paper for IDG2001 Cloud Technologies
Date: 2025-08-??
Time: 09:00

Course contact: Paul Knutson
Present at the exam location: No

Permitted examination support material: E

OTHER INFORMATION

Read the questions carefully and make your own assumptions. In your answers, explain clearly
what assumptions you have made and how you have understood or limited the assignment.

If there are direct errors or omissions in the assignment set and you cannot make your own
assumptions, please refer to the information about complaints regarding formal errors on the
NTNU website “Explanation of grades and appeals”.

SPECIFIC INFORMATION FOR YOUR COURSE

This exam does not include hand drawings. If you receive hand drawing sheets, this is by mistake.
You will not be able to submit the sheets, and they will not be graded.

Weighting: Weighting of questions will be specified in each of the questions. The examiner(s)
retain the freedom to modify these when needed.

Withdrawing from the exam:
If you wish to submit a blank test/withdraw from the exam for another reason, go to the menu in the
top right-hand corner and click “Submit blank”. This cannot be undone, even if the test is still open.

Access to your answers:
After the exam, you can find your answers under previous tests in Inspera. Be aware that it may
take a working day until any hand-written material is available in “previous tests”.

2/10

IDG2001-V2025-2-KONT

 Exam structure and info

Structure, info and hints

There are no negative point for wrong answers*. Better to guess than skip, if you're unsure.
Read the problems properly. Some may ask for which is wrong, not which is right.
Look through the exam before starting answering. The problems are weighted differently.
The ones which counts the most, are often found later in the exam. Save time for them, or
even begin from the back. There are 100 points in total.
Feel free to answer in either English or Norwegian.

How to keyboard:

On a regular Norwegian Windows keyboard, we can write symbols as follows:

(): shift + 8/9
[]: alt.gr. + 8/9
{}: alt.gr + 7/0
/: shift + 7
\: key left of Backspace
': key left of Enter

On a Norwegian Macbook we can write them as follows:

(): shift + 8/9
[]: option + 8/9
{}: option + shift + 8/9
/: shift + 7
\: option + shift + 7
': key left of 1 (§)

Alt.gr. (Windows) is to the right of Space.
option (Mac) is at the bottom row. The train intersection-y key.
Shift is the arrow up, often left, second to bottom.

Good luck!

*Check-boxes need negative points for, so they have negative points. However, the whole problem
will never give a negative score.

3/10

1 Python

DNS servers receive a domain name (e.g., https://www.drive.google.com) and returns the IP
address to the actual Google server. It's like a phone book for web sites. Now, we want to add an
extra layer on top of this in Python. We want to make a function which receives a URL, checks if
the domain is in a block/override list and returns either override URL or DNS URL.

IDG2001-V2025-2-KONT

We have the dictionary below

override = {
    "google.com": "192.168.0.101",
    "ads.net": 192.168.0.123,
    ...

}

And we want to make the function get_url. It should take URL as an input, in the for exemplified
above, and return the same address with IP instead of domain.

The (existing) function ask_DNS takes in a domain name and returns its IP. E.g.,

>>> ask_DNS("google.com")

123.456.789.012

It does not support things like "drive.google.com" og "google.com/MyFiles". Format should only be
"<second-level domain>.<top-level domain>". Use this function in your code.

You need to parse the URL and replace domain with IP address.

Examples

>>> get_url("https://www.drive.google.com/MyFiles"
https://www.drive.192.168.0.101/MyFiles  # Using the override

>>> get_url("https://www.drive.google.com/MyFiles"
https://www.drive.123.123.123.123/MyFiles  # Not found in override; use ask_DNS.

Write your answer in the box below. Changes are saved automatically.

1

4/10

IDG2001-V2025-2-KONT

Maximum marks: 10

5/10

2 HTTP methods

Describe the HTTP methods and what they do.

Write your answer in the box below. Changes are saved automatically.

IDG2001-V2025-2-KONT

Words: 0

Maximum marks: 10

6/10

Format                       Σ 

3 OSI

Describe the OSI model.

Write your answer in the box below. Changes are saved automatically.

IDG2001-V2025-2-KONT

Words: 0

Maximum marks: 10

7/10

Format                       Σ 

IDG2001-V2025-2-KONT

4 Virtualization and containerization

Describe the difference between

a virtualized OS (VM) (e.g., Ubuntu in VirtualBox)
a non-virtualized OS (e.g., Windows on your laptop)
a containerized system (e.g., Docker)

and describe what makes some of these more or less suitable for different situations — with a
focus on cloud-related situations.

Write your answer in the box below. Changes are saved automatically.

Words: 0

Maximum marks: 10

8/10

Format                       Σ 

5 Pros and cons of cloud

Describe some of the pros and cons in using cloud based infrastructure like PaaS and IaaS as
compared to non-cloud hosting for web services.

Write your answer in the box below. Changes are saved automatically.

IDG2001-V2025-2-KONT

Words: 0

Maximum marks: 20

9/10

Format                       Σ 

IDG2001-V2025-2-KONT

6 Plant detection app

I have an app idea and I want you to do some discussions and considerations how it could be
implemented and such.

I want plant detection app. You open the app, you take a picture of an app and the app tells you
which plant it is, gives you some info about the plant and shows you more pictures of the plant (so
you can confirm it is correct). You should then be able to upload the picture to its database, so
we'll have more user-generated pictures of the plants.

I want the info about the app to be generated by LLMs (e.g., ChatGPT). I want the app to work on
Apple and Android, and it should also work as a web site.

I hope the user base will grow over the months/years, and so we should also consider how to
scale the system.

Discuss technological choices (with pros and cons), methods for scaling and such, discuss
different architecture choices, business models, cloud service models, etc. This is a very open
questions, so you are free to include everything you think can be relevant to comment on and
discuss.

Write your answer in the box below. Changes are saved automatically.

Words: 0

Maximum marks: 40

10/10

Format                       Σ 

