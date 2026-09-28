Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[1]
'i'
a[2]
'j'
a[0]+a[1]+a[2]
'vij'
a="iam in class"
a[1]
'a'
a[3]
' '
a[4]+a[5]
'in'
a[3]+a[6]
'  '
a="vijayawada is a royal city"
a[16]+a[20]
'rl'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]
'is'
a="vizag is a city of destiny"
a[0]+a[1]+a[2]+a[3]+[4]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[0]+a[1]+a[2]+a[3]+[4]
TypeError: can only concatenate str (not "list") to str
a[-26]+a[-25]+a[-24]+a[-23]+[-22]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a[-26]+a[-25]+a[-24]+a[-23]+[-22]
TypeError: can only concatenate str (not "list") to str
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
"simple is better than complex"
'simple is better than complex'
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
IndexError: string index out of range
a="simple is better than complex"
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
a[-19]=a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a[-19]=a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
TypeError: 'str' object does not support item assignment
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
#slicing
a=codegnan
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a=codegnan
NameError: name 'codegnan' is not defined
a="codegnan"
a[0:5]
'codeg'
a[:4]
'code'
a[4:8]
'gnan'
a[4:
a=[4:]
  
SyntaxError: '[' was never closed
a="work hard until you succed"
  
a=[0:4]
  
SyntaxError: invalid syntax
a[0:4]
  
'work'
a[4:9]
  
' hard'
a[9:15]
  
' until'
a[15:19]
  
' you'
a[19:25]
  
' succe'
a[19:26]
  
' succed'
a="time is very precious"
  
a[0:4]
  
'time'
a[7:12]
  
' very'
a[12:21]
  
' precious'
a="i love python"
  
a[-11:-7}
  
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[-11:-7]
  
'love'
a[-6:-1]
  
'pytho'
a[-6:0]
  
''
a="today is weekend"
  
a=[-16:-11]
  
SyntaxError: invalid syntax
a[-16:-11]
  
'today'
a[-10:-8]
  
'is'
a[-7:]
  
'weekend'
#striding"
  
a="data science"
  
a[::]
  
'data science'
a[::1]
  
'data science'
a[::2]
  
'dt cec'
a="machine learning"
  
a[::4]
  
'miln'
a[::6]
  
'men'
a[::2]
...   
'mcielann'
>>> a[5:]
...   
'ne learning'
>>> a[:9]
...   
'machine l'
>>> a[::7]
...   
'm n'
>>> a="cloud computing"
...   
>>> a[1:11:2]
...   
'lu op'
>>> a[2:14:4]
...   
'ocu'
>>> a[5:13:3]
...   
' mt'
>>> a[4:12:2]
...   
'dcmu'
>>> a="python course"
...   
>>> a[-1:-11:-2]
...   
'ero o'
>>> a[-2:-12:-3]
...   
'sont'
>>> a="python courses'
...   
SyntaxError: unterminated string literal (detected at line 1)
>>> a="python courses"
...   
>>> a[-1:-12:-2]
...   
'ssucnh'
