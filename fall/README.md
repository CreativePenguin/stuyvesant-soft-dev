# Last Class Today!

Here shall the official record of events transpiring in the 2019-2020 season of SoftDev. Each day, a new Devo will update this, in the appropriate period's folder, according to the template below.
---
---

## Thursday 2019-12-13 :: Making Things Move with Javascript :: Jackson Zou

**Interesting Tech News:** [Attack on New Orleans Government Computers](https://www.cnet.com/news/new-orleans-city-computers-offline-after-cyberattack/)

###JS for selecting HTML elements form the DOM:
```
document.getElementsById(<ID>)
document.getElementsByTagName(<TAG>)
document.getElementsByClassName(<CLASS>)
```

###JS for user action awareness:
```
.addEventListener(<EVENT>, <FUNCTION>)
```

###JS for Manipulating HTML elements:
```
document.createElement(<HTML TAG NAME>)
Element.setAttribute(<NAME>, <VALUE>)
Element.getAttribute(<NAME>)
```

Element is the most general class in DOM (akin to Object in Java)

```
in HTML:
<button id="b"> The button </button>

JS:
var dasbut = document.getElementById("b");
dasbut.addEventListener('click', fxnName);
```

###New events have appeared!
'mouseover'
'mouseout'

e is for Event

Event is interface implemented by all events
automatically passed to event handlers (eg ur fxns)

eg, test drive...

```
button.addEventListener('click',
  function(e) {console.log(e)};
);
```

## Tuesday 2019-12-11 :: Making Javascript useful :: by Kevin Cai

**Interesting Tech News:** [Plus.ai's autonomous lorry crosses the U.S. in three days](https://www.bbc.com/news/technology-50742080)

### Homework
Work on posted assignment as a duo

### What is the DOM?
- Stands for Document Object Model
- is a web API for interacting with HTML
- Is a tree representation of a webpage, which can be manipulated through JS.
- JS is used for selecting/interacting with HTML elements from the DOM.

### Some JS mthods used to interact with the DOM:
- document.getElementById(ID);
- document.getElementsByTagName(TAG);
- document.getElementByClassName(CLASS);
- document.addEventListener(EVENT, FUNCTION_NAME);
- document.createElement(TAG_NAME);
- element.setAttribute(NAME, VAL);
- element.getAttribute(NAME);
- element.remove();
- element.addEventListener(EVENT, FUNCTION_NAME);

### Every program is aware of its environment, which includes:
- Where they live
- OS
- Who ran it
- etc

#### More specifically the javascript environment includes:
- The browser
- Dev console
- The DOM

### Other JS advice:
- Use console.log() to debug, and comment them instead of deleting when you don’t need them. You never know when you might need them again.
- Make sure to remember your semicolons!
- Most development happens through dev console

### Helpful links:
- [DOM Documentation](bit.ly/api_dom)
- [DOM Visualizer](bit.ly/domviewer)

---

## Tuesday 2019-12-10 :: But what about JavaScript? :: by Brandon Chen
**Interesting Tech News:** [Man beats AI drone in first race of its kind](https://www.bbc.com/news/technology-50726399)

#### Homework
- Register droplet IPv4 by tomorrow.
- Complete pair programming assignment.

#### What is JavaScript???
Scheme + "Java" = JavaScript

The Big Idea:
Lets give scheme the syntax of Java and mooch off of Java's popularity by calling it JavaScript!

#### JavaScript Features
- Dynamic typing
	- variable type doesn't need to be declared.
- First class functions
	- can be treated like variables (passed and returned)
- Can be
	- object oriented
	- imperative
	- functional

#### JavaScript "Limitations"
- No I/O (networking, storage, graphics)

#### JavaScript Syntax
- Derived from C like other languages (Java, Python, C++, etc).
- Auto-Semicolon-ination!

#### Best Practices
Avoid:
```
function fxnName(args){
	body;
};
```
Do:
```
var fxnName = function(args){
	body;
};
```
or...(but above is better and more flexible)
```
var fxnName = (args) => {
	body;
};
```

## Monday 2019-12-09 :: What happened in the 1990s? :: by Kenneth Chin
**Interesting Tech News:** [7 EV tech trends to watch in 2020](https://interestingengineering.com/7-ev-tech-trends-to-watch-in-2020)

#### Announcements
- Activate github edupack and register droplet ID by 12/11.

#### Jot down Scheme definition of fact(n)
```
(define fact    
  (lambda (n)
    (if (= n 1)
      1   
      (* n (fact( - n 1))))))

```

#### Lynx
Try: `$lynx www.google.com`
- lynx is a web browser
- oldest browser still in use
- fast
- malware impervious (why? because it doesn't use javascript)
- uses cookies now

#### Timeline
- 1990: Windows 3.0/ Macintosh System 6/ neXT machine
- 1992: Lynx in Gopher space
- 1993: Java is in vogue & mosaic: first mainstream graphical web browser
- 1994: Mosaic communications founded in mtn view
- 1995: Scheme + java -> javascript

#### Javascript
#### 2005: JS goes mainstream
- advent of "web2.0"
- Jesse James Garrett:   
*whitepaper on js-driven page updates w/o reload ("asynchronous")
#### JS features
- dynamic typing
- first-class fxns  
can be treated like vars (passed, returned)
- object-oriented
- imperative
---
## Tuesday 2019-11-12 :: rEST??? :: by Biraj Chowdhury
**Interesting Tech News:** [Revolution at Google ](https://www.bloomberg.com/news/articles/2019-11-12/one-google-staffer-fired-two-others-put-on-leave-amid-tensions)

#### Announcements
- Ensure that your API card doesn't use oauth 2.0, or create a new card.

#### API - Application Program Interface
- published set of protocol that can be used to have your program interact with another program/service

#### REST APIs
- Representational State Transfer
- A rest api transmits data back after recieveing a an http(s) request
- Returned data can be in various forms, most common are HTML, XML, JSON
- Most require a key(why?)--To prevent bots from taking advantage of their api

- Making a REST call in python2, use import urllib2

#### JSON library facilitates work with JSON data
- loads() - turns a JSON object string into a dictionary
- dumps() - turns python dict into JSON object string

---
## Thursday 2019-11-07 :: How tasty is your dog food? :: by Tammy Chen

**Interesting Tech News:** [Facebook is being investigated by California for privacy violations
](https://www.cnn.com/2019/11/06/tech/facebook-privacy-violations-california/index.html)

#### Annoucements:
- Update Chrome ASAP / Use Firefox...
	- Check out QAF post OR [this link](https://www.kaspersky.com/blog/google-chrome-zeroday-wizardopium/29126/).
- PClassics
	- Saturday, November 23rd, 2019 @ University of Pennsylvania
	- *Format:* 8 Questions + Teams (at most 4 people)
	- For more information, check out [this link](http://bert.stuy.edu/pbrooks/pclassic)!

#### Secure Copy
- Secure copy (SCP) is a command-line utility that allows the user to securely copy files and directories between two locations.

```
$ scp source destination
```
- The source (src) and destination (dst) should be absolute or relativbe path (paths that are valid).
	- The format is below:
```
$ scp user@host:path user@host:path
```
- Get comfortable using this ... will boost efficiency!
	- -r means recursive
```
$ scp -r USER@SIMPSON:/home/students/2020/thluffy/public_html/*/tmp/...
```
#### Homework
- Vote: [form](http://bit.ly/how2fef)
- All demos: [link](http://homer.stuy.edu/~thluffy/how2fef/)
---
## Thursday 2019-10-31 :: Stylin' :: by Calvin Chu

**Interesting Tech News:** [Imagine the Possibilities: AI helps develop new compressible material](https://www.popularmechanics.com/technology/design/a29459856/new-material-artificial-intelligence/)

#### Announcements:
- p0 demos
	- Overall great
	- Intros (+/-)
- Going forward…
	- ~~demo login/register~~
	- Repeat Qs for audience to hear
	- Adopt 1 betterpractice another team disp’d

#### Cascading Style Sheets (CSS)
- Created to separate presentation of an HTML/XML page from its content
- Not limited to web pages... (paper, etc.)
- Though HTML tags like <center> exist, you should henceforth avoid them
- 3 ways to incorporate CSS into a page:
	- Inline
	- Internal style sheet
	- External style sheet

**Basic Syntax:**
```
PROPERTY: VALUE;
color: lightsteelblue;
border: 100 px;
```

#### Inline Styling
- Syntax: ```<TAG style=”CSS CODE”>```
- eg: 	```<p style=”Color:green”>```
- Add CSS code to the style attribute of HTML tag
- Good for trying things out
- … but if we want all of the sheets the same, it would be tedious to retype

#### Internal Style Sheet
- Add a STYLE element to the section of the page
- Include all CSS code inside the ```<style> … </style>``` block
- Requires addition of a selector so that it is clear what element you are styling
- Syntax:
```
SELECTOR {
	CSS CODE
}
```
- eg:
```
h1 {
	Color: #FF00FF
}
```
#### External Style Sheet
- Create a separate .css file that contains all of your CSS code
-  It cannot contain any other kind of code (including HTML or XML)
- Include a link to the CSS file inside the head section of your page
- Syntax: <br>
eg:
```
<head>
<link rel=”stylesheet”
      type=”text/css”
      href=”STYLE FILE”>
</head>
```
#### Go go web browser inspect!
- Right-click and select inspect
- Interact with styles without having to touch code

#### The div tag
... is a container element; defines a section of code considered to be grouped together

#### Class Attribute
... is an identifier that can be applied to multiple elements. Any HTML element can have this
- eg:
```<div class=”navbar”> … </div>```
 - To access these classes in your css file, put a period in front of the class name:
```css
.navbar {

}
```

#### ID attributes
- HTML elements can also have an ID attribute (identifier to be applied only to a single element)
- eg: ```<div id=”main”> … </div>```

#### PROTIP:
- You can use ID names in tags as the a=href target
- Good for jumping to another section on the same page
```<a href="#main_content"> ... </a>```

#### TAS(K20):
- Replicate the pgn found on the Assignments page, 3 ways.
	- Choose your own lorem ipsum generator (cite)
	- no Flask

---

## Friday 2019-10-18 :: Designing and Documenting :: by Kazi Jamal

**Interesting Tech News:** [India is trying to build the world's biggest facial recognition system](https://www.cnn.com/2019/10/17/tech/india-facial-recognition-intl-hnk/index.html)

#### Design Documents
We reread the information on the assignments document about Project 00 and Task the First. We then continued working in our teams on the design documents for our projects.

#### Submodule Linking
We passed around the token to begin linking our submodules without merge conflicts in class.

#### Homework
Task the First is due on Monday 10-21. We need to bring in 3 hardcopies of our design documents. Our submodules (named as follows: `name_of_team__lastaF-lastbF`) should also be linked in [upgraded-octo-waffle](https://bit.ly/p0-1920) repository and there should be a PDF named design.pdf in the doc folder.

---
## Thursday 2019-10-17 :: Rendering Based Upon Mistakes :: by Nahi Khan

**Interesting Tech News:** [Amazon GO and its Efficiency] (https://www.fool.com/investing/2019/10/18/why-amazon-will-beat-roku-in-connected-tv.aspx)

### AIM: Render mistakes worthwhile

### Task:
Continue working as a group of four devos in creating the "Plan Assignment due Monday", aka the design document.


---
## Tuesday 2019-10-15 :: Plan, design, document, submit :: by Taejoon Kim

**Interesting Tech News:** [The Nintendo Game Boy Is Coming Back to Life, Kind Of](https://www.wired.com/story/analogue-pocket-coming-2020/)

#### Task
* 1 devo/duo: prep to demo
* 2 devo/duo: prep to response

Q: How did you approach this?

"Facilitate adding rows to the courses table"

#### Smart approach:
function taking args representing fields
* can populate its fields via py-CLI inputs or any other front-e
* can incorporate exception handling

It's good to have helper functions for every sequel query

#### Next Task:
Design a software solution for a crowd-sourced knowledge base.
Q: Primary concerns?
Q: What should your design phase yield?

Begin planning your core functionality, project manager, and team name.

#### wiki
1.a website that allows collaborative editting of its content and structure by its users.

"the simplest online database that could possibly work"

---
## Friday 2019-10-11 :: Presentation on What to Consider for College :: by Jun Tao Lei

**Interesting Tech News:** [Facebook's Libra Association has now lost a quarter of its original members](https://www.theverge.com/2019/10/14/20914269/facebook-libra-association-founders-paypal-visa-mastercard-stripe-ebay)

What to consider when looking for a specific college to apply? By: Mr. Zamansky

#### Things to consider for choosing a college
- Urban vs rural setting (environment, culture, ...)
- Community
- Home vs away for housing
- Big vs small college (courses available, how close is the community)
- Why should you consider NY?
- Why should you consider NY for tech? (many tech opportunities in the city)

#### Tech Education
- Bachelor of Science vs Bachelor of Arts
	- B.S. (for engineering)
	- B.A. (emphasize humanities and arts, emotions)
	- Generally similar
	- Depends on the individual
- Other tech majors / minors

#### Tech Education in NY
- Many great programs
- Many great expensive programs
- Expensive out-of-state tuition

#### CS Educations Dirty Secret
- All good CS schools are virtually the same
- Different in things available, core education is the same
- Rankings or prestige does not necessarily mean a better education
- Look for what is right for you at the time

#### It is about culture and fit

#### Hunter Highlights
- Largest CUNY
- Students from > 150 countries
- Rest from website

#### Hunter CS Highlights
- Comphrenensive CS Curriculum
- Computer Vision
- AI
- Computational Linguistics
- Software Engineering
- Robot

#### Hunter CS Community
- ACM
- Programming Team
- WICS
- CUNY2x
	- On campus bootcamp
	- Workshops
	- Tech in residence
	- Internship opportunities
- Daedalus Highlights
	- Tuition awards
	- Residential priority
	- Tailored classes
	- Faculty mentor
	- Cohort activities
	- PArtnership with the NY Tech Industry
	- Laptops
	- Location at the heart of NYC

#### For more information
- http://info.huntercs.org
- Mailing list if you wrote your name down on the sheet

---
## Thursday 2019-10-10 :: Crunch D numBers :: by Derek Leung

**Interesting Tech News:** [Volvo’s first EV will run native Android](https://www.theverge.com/2019/10/9/20906777/volvo-xc40-suv-ev-native-android-auto-google-assistant-maps)

**Interesting Class News:** New seats! (LCT duties will continue in reverse alphabetical order)

#### Announcement: Google Mentorship Program ####
- Year long (last time it was only semester long)
- Teams of 2-4
- Commitment very important
- Interest meeting Friday room 251 after 10th


**Database Info**
- Databases save automagically to reduce hassle
- We haven't learned how to drop tables yet so for now just delte the .db file
- Multiple connections are allowed
- Changes take effect immediately in shell but not until .commit() in py scripts

**Interacting with sqlite in python**

```python
import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo")
c= db.cursor() #faciltate db ops
c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")
db.commit() #save changes
db.close()
```
Dot operators can be used to access fields:

```python
SELECT name, students.id, mark
FROM students, courses
WHERE students.id = courses.id;
#Note that it is necessary to disambiguate fields of the same name in different tables
#Also triple quote is needed for multi-line strings
```

We ended on this piece of code:
```python
q =
  SELECT name, students.id, mark
  FROM students, courses
  WHERE students.id = courses.id;

foo = c.execute(q)
print(foo)
```
What does foo return?
(It returns the cursor object which is c in this case)

---
## Friday 2019-10-04 :: F for Flashdance :: by Henry Liu

**Interesting Tech News:** [Is Facebook mistreating its' employees](https://www.cnbc.com/2019/09/27/facebook-employee-death-was-suicide.html)

#### Solo task:
Same seats, On kts, sketch out a plan for a software solution to the problem of facilitating storage, management, and retrieval of Stuy info.
eg:
stu sched
fac sched
grade data
resource usage(room,fac,etc)
etc

Using data structures available to you post_APCS

#### Trio task:
Collab w/neighbors
Think about these questions:
Q: Did you nataurally gravitate to a model? flowchart? description in words? something eles? why?
Q: What retrieval operations are easy?
Q: ...which?
Q: Biggest organizational obstacles?
Q: Efficient operations? Inefficient?
Q: What would you like to know from your client?
(the school)

Express your plan as clearly as possible in a googledoc named whitepaper00_pdX<teamname>

Give comment access to softdev19-20@stuy.edu and post to QAF with subject whitepaper00_pdX and content team name, team roster, and link


#### Other:
K16 due Monday


---
## Monday 2019-10-07 :: ALL ABOUT DATABASE :: by Jeff Lin

**Interesting Tech News:** [Google's New Pixel 4 XL Leaks](https://www.cnet.com/news/pixel-4-launch-in-8-days-heres-everything-we-know/)

Reminder: Do not post whitepaper00 on the QAF unless it is ready to present!

#### About Databases ####

A **relational databse** is a databse that stores information as a collection of tables.
Data can be linked between tables based on field.
- FIELD - Column data in an RDB
- RECORD - Row in an RDB

**SQL (Structured Query Language** is a standard language designed to wrok with relational databases.
It is used for many major database programs, though implementations may not be compatible.

(MySQL, SQLite (what we're using), Oracle, IBM DB2)

**SQLite** implementation relies entirely on function calls in the parent program (no database server) (in our case, we will be interacting with it through Python functions).
All database information is stored in a **single file**, which simple for backups and deletion.
Data is dynamically typed as values are inserted.

#### SQLite Syntax ####

**CREATE TABLE** - Add a table to a database.

Types:
- TEXT
- INTEGER
- REAL
- NUMERIC (defaults to integer, but can be float)
- BLOB (no suggested type)

```
CREATE TABLE <name> (<column name> <data type>, ...);
CREATE TABLE farm (animals TEXT, count INTEGER, cost INTEGER);
```

Columns can be given a **PRIMARY KEY** attribute, denoting that every entry in that column is unique and cannot be NULL (for those interested in assigning ID values to students). Columns can be given a NOT NULL attribute, denoting that no entry can be NULL.

**INSERT INTO** - Insert a record into a table. NULL can be used in any entry.

```
INSERT INTO <tbl_name> VALUES (<field 1>, <field 2>, …);
INSERT INTO farm VALUES (“cow”, 20, 100);
INSERT INTO farm VALUES (“sheep”, 40, 60);
INSERT INTO farm VALUES (“chicken”, 100, 20);
```

**SELECT FROM** - Show all fields for each entry (record) in table. * can be used to indicate all. WHERE can be used as a filter.

```
SELECT * FROM <tbl_name>;
SELECT <field> FROM <tbl_name>;
SELECT <field> FROM <tbl_name> WHERE id = 0;
SELECT animals FROM farm;
```


#### Python Implementation (to come later) ####
```python
import sqlite3
db = sqlite3.connect("foo")
c = db.cursor()

c.execute("CREATE TABLE roster (name TEXT, userid INTEGER)")
db.dommit()
db.close()
```

---
## Friday 2019-10-04 :: F for Flashdance :: by Henry Liu

**Interesting Tech News:** [Is Facebook mistreating its' employees](https://www.cnbc.com/2019/09/27/facebook-employee-death-was-suicide.html)

#### Solo task:
Same seats, On kts, sketch out a plan for a software solution to the problem of facilitating storage, management, and retrieval of Stuy info.
eg:
stu sched
fac sched
grade data
resource usage(room,fac,etc)
etc

Using data structures available to you post_APCS

#### Trio task:
Collab w/neighbors
Think about these questions:
Q: Did you nataurally gravitate to a model? flowchart? description in words? something eles? why?
Q: What retrieval operations are easy?
Q: ...which?
Q: Biggest organizational obstacles?
Q: Efficient operations? Inefficient?
Q: What would you like to know from your client?
(the school)

Express your plan as clearly as possible in a googledoc named whitepaper00_pdX<teamname>

Give comment access to softdev19-20@stuy.edu and post to QAF with subject whitepaper00_pdX and content team name, team roster, and link


#### Other:
K16 due Monday

---



## Thursday 2019-10-03 :: Thank your parents & flash your neighbors :: by Grace Mao

**Interesting Tech News:** [Microsoft Doesn't Think Windows is Important Anymore](https://www.theverge.com/2019/10/3/20896908/microsoft-windows-satya-nadella-importance-apps-services-android)

#### Do Now:

Q: What HTTPS status code did you observe in response to redirects?

A: 200

If you didn't know this, you should definitely test the print statements below

    from flask import url_for
    from flask import redirect
    app = Flask(__name__)

    @app.route('/')
    def disp_login():

    ...

    @app.route('/auth')
    def authenticate():
      print(url_for('disp_login'))
      print(url_for('authenticate'))
      return render_template('foo.html')

#### Jinja Reminders!!

1. Statements -   {% ... %}
2. Expressions -  {{ ... }}
3. Comments -     {# ... #}

#### Inheritance (that the Government takes half of)

Jinja supports inheritance!!

For example, if you have a base template, **base.html**:

      <!DOCTYPE html>
      <head>
        {% block head %}
        <title> {% block title %} {% endblock %}
          -|- My Foist Template
        </title>
        {% endblock %}
      </head>
      <body>
        {% block content %}
        No hablo queso
        {% endblock %}
        {% block footer %}
        Copyright Mr. Mykolyk
        {% endblock %}
      </body>

If **ditto.html*** extended **base.html**:

    {% extends "base.html" %}

That page rendered by **ditto.html** would look the same as that of **base.html**

If you were to instead add more code, such as in **foo.html**:

    {% extends "base.html" %}
    {% block title %}
      Index
    {% endblock %}

The title block in **foo.html** would override the block in **base.html**

In this case, the block in **base.html** is empty, so nothing is technically replaced, but because 'My Foist Template' comes outside the block right after it, the new title for **foo.html** would be 'Index -|- My Foist Template'

Lastly, if you were to override the head block such as in **new_title.html**

    {% extends "base.html" %}
    {% block head %}
        <title> WE HURRRR!!! </title>
    {% endblock %}

This would result in a total replacement of the title. In the page rendered by **new_title.html**, the title would be 'WE HURRRR!!!'


#### Other:

We worked on K15, which has a new addendum that calls for you to upload pictures of your sitemap and team flag.

Also, Mr. Mykolyk gave us more work by adding K16, in which we can explore inheritance.

---


## Wednesday 2019-10-02 :: S is for Session :: by Leia Park

**Interesting Tech News:** [The Tech Helping Dogs Learn to 'Talk' With Humans](https://www.wired.com/story/the-tech-helping-dogs-learn-to-communicate-with-humans/)

#### Do Now:

	if wkstn_num % 2 == 0:
		procure(KtS, 2)
		create(team_flag)
		create(site_map)
	else:
		login()
		declareDriver(self)
		load(flask_starter_kit)

#### Site Maps:
- What is it?
	- A site map is a helpful visual list of pages of a web site
- Why should I care?
	- It aids designers in planning and providing a systematic layout of a web site

#### Assistive Code:

1. Redirect: when this function is called, it redirects the user to another target location (aka the website in this instance)

		from Flask import redirect

		redirect(URL) -> redirects

		eg,
		@app.route("/")
		def disp_loginpage():
			return redirect("http://www.xkcd.com")

2. url_for: when this function is called, it gives the inputted function's associated route

		from Flask import url_for

		# to generate the URL associated with a Python fxn:
		# another way to put it: pass function name and receive its URL

		url_for(FXN) -> URL

		eg,
		@app.route("/zoo")
		def loo():
			return "welcome to the monkey house"

		url_for("loo") -> "/zoo"

#### Other:
Spent the period working on homework (K#15 Do I Know You?)

---


## Friday 2019-09-27 :: C is for Cookie :: by Sophie Nichol
**Interesting Tech News:** [UPS Now Runs the First Official Drone Airline](https://www.wired.com/story/ups-drone-airline-faa-certification-delivery/)
#### Notes re: python modules:

If ants.py exists in the current working directory...
import ants
...will make functions defined in ants.py available like this: ants.foo()

But your support functions will live in /utl, so use python package functionality

#### This will make python view utl as a package:
	path/to/flask_app$
	touch utl/__init__.py
Notes:
- __init__.py is a special file that flags a directory as a package directory
- __init__.py can (and should) be empty for now

#### Note: with these files in /utl:

	__init__.py
	ants.py

    ...this code in app.py will load module ants from package utl:

   	import utl.ants as ants
		OR
	from utl import ants

    ...and then make functions defined in ants.py available like so:

    	ants.foo()

#### HTTP Request Methods:
    GET:
     - passed through query string
     - has size limit (2048 chars)
     - less secure, since it can be seen in URL
    POST:
     - sent in background
     - no size limit
     - not more secure, just harder to see

#### Specifying request types:
	Note: GET is default, but you can specify the request type in HTML using the tag attribute
	   eg
		<form action="/login" method="GET">
		<form action="/login" method="POST">

	You can also specify which requests to handle in flask
	   GET only (use either):
		@app.route('/login')
		@app.route('/login', method=["GET"])
	   POST only:
		@app.route('/login', method=["POST"])
	   Both:
		@app.route('/login', method=["GET", "POST"])

#### COOKIE:
 - small file given by the website to a web browser for storage on you LOCAL machine
 - useful for maintaining awareness of identity across multiple page visits on the same site
 - transmitted with request

 #### How do you get cookies?
      request.cookies.get(KEY)
          - accesses cookie data if available (no error thrown if key missing)
        eg
  	   request.cookies.get('username')

#### S is for SESSION:
	Flask module to facilitate "remembering" users from one request to the next

	Flask session data is maintained by the server but stored in cookies on the client:
 		- cookie payload is encoded
 		- any HTTP transmission is "sniffable"
 		- flask session onject works like a dict
 		- cookie is securely signed (similar to Github private/public mechanism)

#### Note: on the security of flask session cookies:
	Data is encoded - not encrypted

	An encoding scheme (ASCII, unicode, etc) ensures data transfer, consumtion with reliability/repeatability/intergrity
 		- 2-way, anyone who knows schema can go either way

 	An encrytion alogorithm (ex AES, RSA) esnures data privacy
  		- need private key to unlock transmission

 	A stranger can view this cookie data, but not change it

 #### Q: What must you do to ensure a private session?
 #### A: Generate a private key, and assign as built-in secret_key
 	app.secret_key = <randomly_generates_string>

 	to get randomized string:
 		import os
		os.urandom(32) --> produces 32 bits of random data as a string

	Maxim:
	Never, ever store a private key in a publicly-viewable location (like your workshop)

	Eg: from flask import session
		to add data to a session:
			session[KEY] = value
		to remove data from session:
			session.pop(key)

---  

## Thursday 2019-09-26 :: Learning Hosting Manners to Greet Your Visitors :: by Connor Oh
**Interesting Tech News** [Helping Refugees Get Fed with Iris Scanners](https://www.digitaltrends.com/cool-tech/world-food-programme-building-blocks-iris-scanning-blockchain/)
#### The Importance of Pair Programming
As shown by the experiences of various Stuy Alumnis, pair programming is a key feature for future careers with coding.
#### Adding On To Diagnostic Print Statements
Break them up with some line break print statements

Now here's an example from yesterday:
```
@app.route("/auth")
def authenticate():
	print(app)
	print(request)
	print(request.args)
	return "waaaaaaaaahooooHHAAAHHAA"
```

Now this is okay, but sometimes it can be hard to see what diagnostic is what when looking at the flask terminal
So this calls fro some breaking up
Here are some example:
```
@app.route("/auth")
def authenticate():
	print("/////////////!!!\\\\\\\\\\\\\\")
	print(app)
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print(request)
	print("==============================")
	print(request.args)
	return "waaaaaaaaahooooHHAAAHHAA"
```

But we can do better
Let's be more descriptive now so we know which diagnostic statement is saying what
```
@app.route("/auth")
def authenticate():
	print("\n\n\n")
	print("***DIAG: THIS FLASK OBJ***")
	print(app)
	print("***DIAG: REQUEST OBJ***")
	print(request)
	print("***DIAG: request.args***")
	print(request.args)
	#print("***DIAG: request.args['username']***")
	#print(request.args['username']) (the inputted username from form)
	#print("***DIAG: request.headers***")
	#print(request.headers) ----> shows "the content type of the response payload and a time limit on how long to cache the response" according to (https://realpython.com/python-requests/)
	return "waaaaaaaaahooooHHAAAHHAA"
```
#### TASK
We worked on the homework
#### HOMEWORK
Your (duo) job:

-Write a Flask app to serve a 2-page website (a landing page at / and a response page at /auth) to echo to a user their input via an HTML form. Your app's response should be rendered via template, and the following should be viewable in the browser:

	On both pages:
		-your team name and roster
	On response page:
		-username entered
		-request method used
		-your greeting to this person

---

## Wednesday 2019-09-25 :: A Formal Request for Environmental Awareness :: by Lauren Pehlivanian
**Interesting Tech News** [Analyzing Tsunamis using Amateur Video](https://www.wired.com/story/amateur-video-helping-understand-deadly-tsunamis/)
#### How are forms submitted?
You need a back end to process the form data after the user presses Submit.
#### Creating a Form in HTML
**Task:** Whip up an HTML page with text input field and a submit button.
```
<body>
	<form action="/auth">
		<input type="text" name="username">
		<input type="submit" name="sub1">
	</form>
</body>
```
- "/auth" represents the route a user will be directed to after clicking Submit. We need to create a new /auth route in the Flask app.
#### Viewing Form through Flask
**Task:** Write a Flask app with the root route rendering the HTML file as template.
** No Jinja is necessary!
#### How Form Data is Stored
- cgi.FieldStorage: immutable dictionary generated by form submission.
#### Python's way of stringifying an Object
**Task:** Insert ```print(app)``` into Flask app-- what is printed out?
- Output: ```<Flask "app">```
- This is Python's way of stringifying an Object: ```<classname 'var_name'>```
#### Flask Request Object
- Flask's request object stores info about an incoming request.
##### Its useful fields:
```request.headers```: HTML headers from client browser <br />
```request.method```: GET or POST <br />
```request.args```: arguments, as querystring from GET request; immutable dictionary <br />
```request.form```: arguments sent via POST request; immutable dictionary <br />
Add Flask request to import statements:
```
from flask import Flask
from flask import render-template
from flask import request
```
#### elucidation TASK
Figure out via console messages some keys in request dictionaries.
#### Homework
- Update name on Github to your full name!

---

## Tuesday 2019-09-24 :: rateyourclassmates.com :: by Winston Peng  
**Interesting Tech News** [Facebook Buys CTRL-Labs](https://www.wired.com/story/facebooks-latest-purchase-gets-inside-users-headsliterally/)  
#### Gitignore and Better Organization  
Adding a gitignore will ensure that you don't have trash in repo (eg. \_\_pycache\_\_ folder).
 Check [QAF Post](https://github.com/stuy-softdev/notes-and-code19-20/blob/master/smpl/00gitterdun/dot_gitignore)
which also ignores .DS\_Store files that appear on macs.  
Additionally, if you're planning on going above and beyond, make sure that you create a separate folder to store your code.
Eg. if you have extra software for `10_occ`, store it in folder `10_occ_extrafolder`.  
#### Code Review Goals
- Improve understanding of code base (handy if peeps ditch)  
- Copy other people's coding habits (check out Python Style Guides if interested)  
- Build stakeholder confidence (kinda like showing your work on a test)  
- Pride/reward (you'll write better code if you know other people are going to read it)  
- Perspective "another set of eyes" -- adds objectivity -- Can easier identify defects  
#### Today's Goals  
- Spread Jinja/Flask fluency  
- Promote best practices  
- Suppress worst practices  
- Identify core vs extended functionality  
#### Things To Focus On In Code Review  
- General unit testing (Clone repo and make sure it runs)  
- Comment & Coding conventions (don't overkill comments, and name variables good)  
- Control Structures (eg. splitting up methods)  
#### Activity
- Pull (Devo +5)'s work repo  
- Review their code  
- Run their flask app
- Fill in sheet "Code Review" (basically the things to focus on in code review, except you give a 1-4 grade for each point)  

---  

## Monday 2019-09-23:: Jinja Tuning :: by Jude Rizzo

**Interesting Tech News** [Satellites Getting Hacked](https://www.bbc.com/news/technology-49768617)

#### Some links to catch up on
* [bit.ly/jinja0]
-This has some information on flask and jinja, it’s a good link to copy down.
-Focus on the sections for variables, comments, and the list of control structures, such as for and if.

* [pallersprojects.com]
-This is a link where you can read Flask, Jinja, and Werkzeug pages

*[bit.ly/2kQ2Hc7]
-This is about the configurations and conventions of using flask

* In addition to showing us these links, we were also reminded to check our repositories to make sure they were properly set up with appropriate headings and comments in our code.

* Then we worked on the homework due tomorrow.

#### Homework
* Due tomorrow is the Jinja Tuning Duo assigment

---  

## Friday 2019-09-20 :: Slot in the missing piece :: by Calvin Chu

**Interesting Tech News:** [Chrome Catching Up](https://www.theverge.com/2019/9/20/20875441/google-chrome-tab-management-improvements-color-customization-features)

#### Using Jinja in HTML
 ```
<!DOCTYPE html>
 <html>
   <head>
     <title> {{ foo }} </title>
   </head>
   <body>
     {% for item in collection %}
       {{ item }}
       <br>
     {% endfor %}
   </body>
 </html>
 ```
#### Displaying a Jinja Template
* Create a "templates" directory on the same level as /static to house your HTML_TEMPLATE.html
* In addition to importing flask, another Flask module is needed to use the Jinja2 templating engine:
 ```
	from flask import Flask, render_template
 ```
* render_template provides the render_template method:
 ```
	render_template("HTML_TEMPLATE", var1name = var1val1, var2name = var2val2, ...)
 ```
* In app.py, return the render_template method to display on the website.  
* Example:
 ```
col = [1, 1, 3, 5, 8]

 @app.route("/my_foist_template")
 def test_tmplt():
   return render_template(
     'my_foist_template.html',
     foo = "foooooo",
     collection = col
     )

 ```
The website should display the items in col on separate lines.
#### Homework
* Use the templating engine to publish occupation info from assignment 03 (see HW page for more details)
---
## Thursday 2019-09-19 :: Essence of Templating :: by Manfred Tan

**Interesting Tech News:** [Huawei vs the Google!](https://www.bbc.com/news/technology-49754376)

#### Productive dev workflow
* For most of our code, we should be developing incrementally. That means making the code work using the bare minimum, then adding more as we go.
* Pair Programming: driver + navigator = awesome
  * like rally racing
  * one person types while the other observes/guides/thinks
  * both devos get smarter faster
  * take turns in each role
  * it is not a race

#### Adding to our Flask app
* PPTask:
  * set up static folder and load pages from it.
  * static folder should be in the same directory (level) as app.py, your main file.
* Create a standard HTML file:
  ```
      <!DOCTYPE html>
      <html>

      <head>
            <title>  </title>
      </head>

      <body>
            <h1>  </h1>
      </body>

      </html>
  ```

* Augment this file with filler, then copy it into the static folder. Make sure the flask web server is running.
  * When the file is on your computer, you can render it by doing: file://path/to/file.html
  * To display on web server, we can do: 127..../static/poo.html (poo is our html file)
* Templating engine:
  * We can write HTML code in python by concatenating strings with the HTML code inside, but it gets confusing and messy. So we use a templating engine to write code directly into the HTML file.
  * Jinja2 facilitates
   * separation of content from design
   * reduction of repetition
  * by using
   * conditionals
   * looping structures
   * etc
* example of Jinja2 syntax:
   ```
   {% if a %}
   tempvar a has value {{a}}
   ```

  * {{a}} will be replaced with the actual value of a.

  ```html
        <title> {{foo}} </title>
        <body>
            {% for item in collection %}
                  {{item}}
            <br>
            {% end for %}
  ```
* We can render an HTML file using the render_template() function.

---

## Wednesday 2019-09-18:: Fill yer flask :: by Ahmed Sultan

**Interesting Tech News:** ['IBM's new 53-qubit quantum computer is its biggest yet'](https://www.cnet.com/news/ibm-new-53-qubit-quantum-computer-is-its-biggest-yet/)

#### Breaking apart a route in Flask

```python
@app.route("/")
def hello_world():
      print(__name__)
      return "No hablo queso!"
```

* The decorator, or ```@app.route("/")``` in the above code snippet, is responsible for telling the app what should be viewed by the user.
  * The "/" contained within the parameters of the decorator stands for the root of your app — essentially, the default page that loads when you go to an address.
  * This "/" can be changed to anything valid (i.e. "/sultan", "/softdev", "/mykolyk")
* The function (```def hello_world():```) immediately following the routing decorator shows what should be shown on the page.
  * The print statement is what is returned in the Flask console when a page is requested.
  * The return statement is what is shown on the page being viewed by the user.

#### What should go with a Flask app?

* Directory: /static -- what should be stored here?
  * images
  * static HTML
  * CSS files
* Directory: /data -- what should be stored here?
  * CSV files
  * inert data

#### Homework

* Create a Flask app with three working routes. Watch the Flask console as you work.

---
## Tuesday 2019-09-17 :: What's in yer flask? :: by Albert Wan

### Interesting Tech News: Weed Killing Robots:
https://www.digitaltrends.com/cool-tech/farmwise-weed-killing-robot/
#### A web framework is described as:
- A software framework that is dseigned to support development of web applications including web servers, web resources, and web API's
- Web frameworks aim to automate the overhead associated with common activities performed in web development.

#### Why a web framework?
- FOSS
- Micro-Framework
- Rapid prototypes
- Production-grade
- You know and love python
- Widely used

#### Examples of web framework
- PHP: Silex
- Java: Spark
- Cold fusion: ColdBox
- Python: Flask

## Flask properties
Has its own development web server
Includes few modules: Werkzeug and Jinja
Flask will serve a page user when they either:
1. a route for the page is defined in the flask app
2. the page is stored in /static

## What does CGI stand for?
Common Gateway Interface: standard protocol fo a webserver to excecute programs.

## Code we ran at the end of class:
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
print(__name__)
return "no hablo queso!"

if __name__ == "__main__":
app.debug = True
app.run()
```
---
## Monday 2019-09-16 :: What is a virtual environment? :: by Jason Zheng

#### The Encyclopedia Britannica defines computer science or computing science as the:
Study of computers, their design (architecture), and their uses: **computation, data processing, and systems control**, including design and development of hardware and software and programming.

The field encompasses **theory**, mathematical activities such as **design and analysis of algorithms**, **performance studies** of systems and their components, and estimation of reliability and availability of systems by **probabilistic techniques**.

Because computers are often too large and complicated for failure or success of a design to be predicted without testing, **experimentation** is built into the development cycle.

#### Wikipedia defines CS as the study of the theoretical foundations of computation and of practical implementation of this theory in computer systems.

#### Why this course?
* Rise of browser-as-OS
* U R h4x0r
* Bring it all together
* Make it work -T.Gunn

#### What will we do?
* Transmogrify you into a full stack developer
* Get dirty but with intent
* Experience multiple roles
* Demo --> test drive --> expand --> expand more --> share --> incorporate

#### What will we use?
Examples
* Flask
* Python
* SQLite
* MongoDB

StuyCS tool/platform selection criteria:
FOSS (Free and open-source software) + ubiquity + robustness + simplicity + scale/growth

from homedir...

    $ python3 -m venv hero         #hero can be anything
    $ . hero/bin/activate          #DOT('.') is equivalent to bash's source command; it runs a script
    (hero)$ pip3 install flask
          <write and run Flask code...>
    (hero)$ deactivate

from working dir...

    $ . ~/hero/bin/activate
    (hero)$ pip3 install flask
          <write and run Flask code...>
    (hero)$ deactivate
          <now you're back to normal environment>

#### PROTIP: Devote a separate terminal to running Flask apps

---
## Friday 2019-09-13:: Helpful web developing stuff we will use in the future :: by Jackson Zou

**Interesting Tech News:** [Youtube's Misleading Algorithm](https://www.bbc.com/news/blogs-trending-49483681)

#### Overview of Web Developing Stuff from Intro2
* Web Server -> Apache 2
* #!/bin/... was the file path
* homer.stuy.edu/~user was URL used for access
* it looked for the public_html directory assuming permissions were allowed and defaulted to running index.html

#### What we will use now because we are big boys and girls
* Flask
* CGI

#### Homework
* work on occupations.csv stuff with partner
* Bring ducks


---

## Tuesday 2019-09-05 :: BLISSFUL RESPITE, I HARDLY KNEW YE :: by Clyde "Thluffy" Sinclair

**Interesting Tech News:** [Gimme the Juice!](https://www.bloomberg.com/news/articles/2019-09-12/a-car-running-on-empty-isn-t-impossible-if-toyota-gets-its-way)

#### Stuff
* Blah
* Blah
* Blah

Note the horizontal line below. Use it effectively.

---
