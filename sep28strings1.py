Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
#find a string
a="python"
a.find("h")
3
a.find("n")
5
b="hello"
b.find("l")
2
b[2:4]
'll'
#escape sequances
#\n->new line
#\t->tap space
a="name\nmobileno\tcollege\nmailid\tbranch"
print(a)
name
mobileno	college
mailid	branch
b="revathi\nmobileno:7324566265\tcollege:D.N.R\nmailid:revathikatta81@gmail.com\tbranch:bsc"
print(b)
revathi
mobileno:7324566265	college:D.N.R
mailid:revathikatta81@gmail.com	branch:bsc
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python c"
b.replace("c","dsa')
          
SyntaxError: unterminated string literal (detected at line 1)
b.replace("c","dsa")
          
'python dsa'
#upper
          
a="code"
          
a.upper()
          
'CODE'
#lower
          
b="python"
          
b="HELLO"
          
b'lower()
          
SyntaxError: unterminated string literal (detected at line 1)
b.lower()
          
'hello'
c="python"
          
c[0].upper()
          
'P'
c.capitalize()
          
'Python'
d="python course"
          
d.title()
          
'Python Course'
e="i am in class"
          
e.capitalize()
          
'I am in class'
# true or false
          
a="java"
          
a.isupper()
          
False
a.islower()
          
True
b="PYTHON"
          
b.isupper()
          
True
c="'
          
SyntaxError: unterminated string literal (detected at line 1)
c="name"
          
c.endswith()
          
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c.endswith()
TypeError: endswith expected at least 1 argument, got 0
c.endswith(e)
          
False
f=1212
          
f.isdigit()
          
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    f.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
f="234"
          
f.isdigit()
          
True
e="revathi@123"
          
e.isalnum()
          
False
type(f)
          
<class 'str'>
#strip()
          
#lstrip(0,rstrip()
          
a="      revathi      "
          
a.strip()
          
'revathi'
a.lstrip()
          
'revathi      '
a.rstrip()
          
'      revathi'
#concatination
          
a="code"
          
b="gnan'
          
SyntaxError: unterminated string literal (detected at line 1)
b="gnan"
          
print(a+b)
          
codegnan
a="python"
          
b="course"
          
print(a+b)
          
pythoncourse
print(a+" "+b)
          
python course
fname="revathi"
          
lname="katta"
          
print(fname+lname)
          
revathikatta
print(fname+" "+lname)
          
revathi katta
print((fnmae.title()+" "lname.title())
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print((fname+" "+lname).title))
          
SyntaxError: unmatched ')'
print((fname+" "+lname).title())
          
Revathi Katta
#spilt
          
a="c c++ python java"
          
a.spilt()
          
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.spilt()
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
a.split()
          
['c', 'c++', 'python', 'java']
b="i am learning python fullstack"
          
b.split()
          
['i', 'am', 'learning', 'python', 'fullstack']
#join()
          
a="apple","banana","grapes"
          
"'.join(a)
          
SyntaxError: unterminated string literal (detected at line 1)
"".join(a)
          
'applebananagrapes'
" ".join(a)
          
'apple banana grapes'
"l".join(a)
          
'applelbananalgrapes'
#formating
          
a=3
          
b=6
          
print(a+b)
          
9
print("the sum is",a+b)
          
the sum is 9
city="vij"
          
print("city is",city)
          
city is vij
#format method()
          
a="motu"
          
b="patlu"
          
print("hello {}".format(a,b))
          
hello motu
print("hello {}{}".format(a,b))
          
hello motupatlu
print("hello {} {}".format(a,b))
          
hello motu patlu
print("hello {} hello{}".format(a,b))
          
hello motu hellopatlu
print("hello {}{}".format(a,b).title())
...           
Hello Motupatlu
>>> print("hello {} hello{}".format(a,b)).title())
SyntaxError: unmatched ')'
>>> print("hello {} hello{}".format(a,b).title())
Hello Motu Hellopatlu
>>> #formatingstring
>>> #fstring
>>> a="revathi"
>>> b="k"
>>> print(f"hello {a}{b}")
hello revathik
>>> print(f"hello {a} {b}")
hello revathi k
>>> print(f"hello{a} hello{b}")
hellorevathi hellok
>>> a=12
>>> b=34
>>> print(f"sum of {a}+{b}")
sum of 12+34
>>> print("the produt is {}".format()")
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("the produt is {}".format())
...       
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    print("the produt is {}".format())
IndexError: Replacement index 0 out of range for positional args tuple
>>> a=3
...       
>>> b=5
...       
>>> c=a*b
...       
>>> print("the priduct is {}.format(c)")
...       
the priduct is {}.format(c)
>>> print("the priduct is {}".format(c))
...       
the priduct is 15
