Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#assignment
a=5
b=6
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
11
a-=4
a
7
a*=5
a
35
a//=2
a
17
a/=5
a
3.4
a**=6
a
1544.8044159999997
a%=3
a
2.804415999999719
b
6
b+=2
b
8
b-=3
b
5
b*=4
b
20
b//=5
a
2.804415999999719
b/=3
b
1.3333333333333333
b**=6
b
5.618655692729765
b%=7
b
5.618655692729765
#comparision
a=6
b=5
a<b
False
a>b
True
B<a
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    B<a
NameError: name 'B' is not defined. Did you mean: 'b'?
b>a
False
b<a
True
a<=a
True
b>=a
False
a!=b
True
a==b
False
a=5
b=5
a==b
True
#logical
a=10
b=20
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a NameError: name 'B' is not defined. Did you mean: 'b'?
SyntaxError: invalid syntax
a<=b or b>=a
True
a!=b or a==b
True
#identify
a=3
type
<class 'type'>
type(a) is int
True
type(a) is not int
False
type(a) is not float
True
#membership
a=3.5
type
<class 'type'>
type(a) is float
True
type(a) is not float
False
type(a) is boolean
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    type(a) is boolean
NameError: name 'boolean' is not defined
type(a) is bool
False
type(a) is not complex
True
type(a) is str
False
#membership
a=1,2,3,4,5,6,7,8,9,10
9 in a
True
15 in a
False
17 not in a
True
30 in a
False
#bitwise
#bitwise
a=4
b=6
a&b
4
bin(4)
'0b100'
bin(6)
'0b110'
a=2
b=4
a/b
0.5
a|b
6
>>> a=5
>>> b=7
>>> a|b
7
>>> a=5
>>> ~a
-6
>>> -(a+1)
-6
>>> a=-7
>>> ~a
6
>>> -(a+1)
6
>>> a=4
>>> b=5
>>> a^b
1
>>> a=3
>>> b=6
>>> a^b
5
>>> a=4
>>> a<<2
16
>>> bin(a)
'0b100'
>>> a=8
>>> a<<3
64
>>> a>>2
2
>>> a>>3
1
>>> a>>3
1
>>> a=9a>>3
SyntaxError: invalid decimal literal
>>> a=9
>>> a>>3
1
