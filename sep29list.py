Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=9.6
type(b)
<class 'float'>
c=[8.3]
tupe(c)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tupe(c)
NameError: name 'tupe' is not defined. Did you mean: 'tuple'?
type(c)
<class 'list'>
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
a=["ds","ai"]
a.extend(["c","c++")
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a.extend(["c","c++"])
         
a
         
['ds', 'ai', 'c', 'c++']
#insert
         
b=["python","java","c"]
         
b.insert(1,"ds")
         
b
         
['python', 'ds', 'java', 'c']
a=["hyd","vij","viz"]
         
a.index("viz")
         
2
a.copy()
         
['hyd', 'vij', 'viz']
b=a=["hyd","vij","viz"]
         
b
         
['hyd', 'vij', 'viz']
c=a.copy()
         
c
         
['hyd', 'vij', 'viz']
#sort()
         
a=["mango","apple","grapes","banana"]
         
a.sort()
         
a
         
['apple', 'banana', 'grapes', 'mango']
b=[2,5,6,3,4,7,8,1,43]
         
b.sort()
         
b
         
[1, 2, 3, 4, 5, 6, 7, 8, 43]
a=["grapes","Apple","Mango","berry","Berry"]
         
a.sort()
         
a
         
['Apple', 'Berry', 'Mango', 'berry', 'grapes']
b=["Kiwi","apple","Banana","berry"]
         
b.sort()
         
b
         
['Banana', 'Kiwi', 'apple', 'berry']
#reverse()
         
a=["black","white","red","blue"]
         
a.reverse()
         
a
         
['blue', 'red', 'white', 'black']
b=[5,4,7,3,9,]
         
b.reverse()
         
b
         
[9, 3, 7, 4, 5]
#pop(0
         
a=["java","ds","ai"]
         
a.pop()
         
'ai'
a.pop(0)
         
'java'
a
         
['ds']
a.remove()
         
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
a.remove(ds)
         
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.remove(ds)
NameError: name 'ds' is not defined
>>> a.remove("ds")
...          
>>> a
...          
[]
>>> b=["chair","table"]
...          
>>> b.clear()
...          
>>> b
...          
[]
>>> c=[]
...          
>>> c.append("revathi")
...          
>>> c
...          
['revathi']
>>> #length count
...          
>>> a=["hi","hello"]
...          
>>> len(a)
...          
2
>>> b="hello"
...          
>>> len(b)
...          
5
>>> c=["hello"]
...          
>>> len(c)
...          
1
>>> a.count("hi")
...          
1
