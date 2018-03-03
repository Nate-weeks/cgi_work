#!/usr/bin/env python3                                                                               
import cgi
import os
import cgitb
import datetime
import random
#from cookie import simplecookie
#from http import cookies
cgitb.enable()
import re



'''
expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = Cookie.SimpleCookie()
cookie["session"] = random.randint(1000000000)
cookie["session"]["domain"] = ".jayconrod.com"
cookie["session"]["path"] = "/"
cookie["session"]["expires"] = \
  expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")

print ("Content-type: text/html")
print (cookie.output())
print ()
print ("Cookie set with: " + cookie.output())
'''

def main():
	form = cgi.FieldStorage()
	name = form.getfirst("name", "default name")
	cookie = str(random.randint(100, 1000000000))
	color = getColor()
	cookieColor = color
	print("Content-Type: text/html\nSet-Cookie: color=" + cookieColor + "\nSet-Cookie: session=" + cookie + "\n")

	print("""
	<html>
  	<Title>Hello in HTML</Title>
	<body>
	<form action="namesaver.py" method="get">Your Name: <input maxlength="60" size="60"  name="name">
	<input value="Submit Name" type="submit">
	<form action="namesaver.py" method="get">Your Favorite Color: <input maxlength="60" size="60"  name="color">
	<input value="Submit Color" type="submit">
	</form>
	</body>
	</html> """)
	
	contents = processInput(name, color)
	print(contents)
	if "HTTP_COOKIE" in os.environ:
    		print (os.environ["HTTP_COOKIE"])
	else:
    		print ("HTTP_COOKIE not set!")

def processInput(name, color):
	'''Process the name by saving it to a file and returning it as an html greeting'''
	greetingName = name
	favoriteColor = color 
	return fileToStr('nameTemplate.html').format(**locals())


def getColor():
	form = cgi.FieldStorage()
	from_cookie = re.search(r'color=(\w+)', os.environ["HTTP_COOKIE"])
	from_form = form.getfirst("color", "red")
	color = ''
	if from_form:
		color = from_form
	elif from_cookie:
		color = from_cookie.groups()[0]
	if color:
		return color
	else:
		return 'orange'

def fileToStr(fileName):
	fin = open(fileName);
	contents = fin.read();
	fin.close()
	return contents

try:
	main()
except:
	cgi.print_exception()
