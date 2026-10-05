Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"revathi","year":2026,"month":9}
print(a)
{'name': 'revathi', 'year': 2026, 'month': 9}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['revathi', 2026, 9])
a.items()
dict_items([('name', 'revathi'), ('year', 2026), ('month', 9)])
#accessing[]
a={"name",:"revathi","city":"vij"}
SyntaxError: invalid syntax
a["name"]
'revathi'
a.get("name")
'revathi'
a.get("revathi")
a
{'name': 'revathi', 'year': 2026, 'month': 9}
a["revathi"]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a["revathi"]
KeyError: 'revathi'
#pop
a={"city":"vij","state":"ap","country":"india"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("state")
'ap'
a
{'city': 'vij', 'country': 'india'}
#popitem
a.popitem()
('country', 'india')
a
{'city': 'vij'}
#update
a={"course":"python","duration":100}
a
{'course': 'python', 'duration': 100}
a.update({"month":"sep"},{"date":30})
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.update({"month":"sep"},{"date":30})
TypeError: update expected at most 1 argument, got 2
a.update({"month":"sep","date":30})
a
{'course': 'python', 'duration': 100, 'month': 'sep', 'date': 30}
#setdefault()
a={"date",:30,"time":11}
SyntaxError: invalid syntax
a={"date":30,"time":11}
a.setdefault("hour":11)
SyntaxError: invalid syntax
a.setdefault("hour",11)
11
a
{'date': 30, 'time': 11, 'hour': 11}
>>> #copy
>>> a={"colour":"white","food","biryani"}
SyntaxError: ':' expected after dictionary key
>>> a={"colour":"white":"biryani"}
SyntaxError: invalid syntax
>>> a={"colour":"white","food":"biryani"}
>>> a.copy()
{'colour': 'white', 'food': 'biryani'}
>>> len(a)
2
>>> a.count("date")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.count("date")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("date")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.index("date")
AttributeError: 'dict' object has no attribute 'index'
>>> a.clear()
>>> a
{}
>>> a={"name":"revathi","city":"vij","name":"revathi"}
>>> print(a)
{'name': 'revathi', 'city': 'vij'}
>>> a={"name":"revathi","city":"vij","name":"revathi"}
>>> a
{'name': 'revathi', 'city': 'vij'}
>>> a
{'name': 'revathi', 'city': 'vij'}
>>> a={"idnos":10,20,30}
SyntaxError: ':' expected after dictionary key
>>> a={"idnos":[10,20,30],"names":["anu","rev","sam"}
...    
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a={"idnos":[10,20,30],"names":["anu","rev","sam"]}
...    
>>> a
...    
{'idnos': [10, 20, 30], 'names': ['anu', 'rev', 'sam']}
