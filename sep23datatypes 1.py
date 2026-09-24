Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
b=8.7
type(b)
<class 'float'>
a=6+7j
type(a)
<class 'complex'>
"python"
'python'
a="python"
type(a)
<class 'str'>
m="j"
type(m)
<class 'str'>
z=True
type(z)
<class 'bool'>
#datatype
#integer
int(1)
1
int1.3)
SyntaxError: unmatched ')'
int(1.7)
1
int("class")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int("class")
ValueError: invalid literal for int() with base 10: 'class'
iny(1+4j)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    iny(1+4j)
NameError: name 'iny' is not defined. Did you mean: 'any'?
int(1+4j)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(1+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#float
float(3)
3.0
float(3.6)
3.6
float("class")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    float("class")
ValueError: could not convert string to float: 'class'
float(3+4j)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float(3+4j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str
str(1)
'1'
str(2.5)
'2.5'
str("class")
'class'
str(3+4j)
'(3+4j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(1)
(1+0j)
>>> complex(2.6)
(2.6+0j)
>>> complex(2=7j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> complex(2+5j)
(2+5j)
>>> complez("class")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complez("class")
NameError: name 'complez' is not defined. Did you mean: 'complex'?
>>> complex("class")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    complex("class")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(1)
True
>>> bool(2.3)
True
>>> bool(2+6j)
True
>>> bool("class")
True
>>> bool(True)
True
>>> bool(False)
False
