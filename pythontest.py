#!/usr/bin/env python3
import cgi 

print("Content-Type: text/html\n\n")  # html markup follows

def main():
	form = FeildStorage()
	name = form.getfirst("question","sorry you messed up")
	print("""
<html>
<Title>Hello in HTML</Title>
<body>
Stupid tester for leslie
<form action= "pythontester.py" method="get">Who is the queen of the world?<input name="question">
<input value="submit queen" type="submit">
</form>
%s 
</body>
</html> """ % name) 
