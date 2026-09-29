Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
a=(4,6.7,"revathi",8+9j,True,False)
print(a)
(4, 6.7, 'revathi', (8+9j), True, False)
type(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(b)
NameError: name 'b' is not defined
type(a)
<class 'tuple'>
a.count(8+9j)
1
a.index(True)
4
len(a)
6
#sets()
#sets{}
a={3,6.7,"python",8+9j,True,False}
print(a)
{False, True, 3, (8+9j), 6.7, 'python'}
type(a)
<class 'set'>
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.issubset(b)
False
b.issubset(a)
False
a={2,3,4,5,6,7,8,}
b=a{5,6,7,8}
SyntaxError: invalid syntax
a={2,3,4,5,6,7,8}
b={5,6,7,8}
a.issubset(b)
False
b.issubset(a)
True
#superset{}
a={4,5,6,7,8,9}
b={7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
a={4,5,6,7,4,5,2,0,7,8}
print(a)
{0, 2, 4, 5, 6, 7, 8}
#union()
a={10,11,12,13,14,15}
b={14,15,16,17,18,19}
a.union(b)
{10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
a
{10, 11, 12, 13, 14, 15}
#intersestion()
a={4,5,6,7,8,9,10}
b={8,9,10,11,12,13}
a.intersection(b)
{8, 9, 10}
#update()
a={3,4,5,6,7}
b={6,7,8,9,10}
a.update(b)
a
{3, 4, 5, 6, 7, 8, 9, 10}
a
{3, 4, 5, 6, 7, 8, 9, 10}
b
{6, 7, 8, 9, 10}
b.update(a)
b
{3, 4, 5, 6, 7, 8, 9, 10}
b
{3, 4, 5, 6, 7, 8, 9, 10}
#difference()
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.difference(b)
{8, 5, 6, 7}
b.difference(a)
{12, 13, 14}
#symmetric difference
a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.symmetric_difference(b)
{3, 4, 9, 10}
#diff update
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.difference_update(b)
a
{4, 5}
b.differnce_update(a)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    b.differnce_update(a)
AttributeError: 'set' object has no attribute 'differnce_update'. Did you mean: 'difference_update'?
b.difference_update(a)
b
{6, 7, 8, 9, 10, 11}
#intersection_update()
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.intersection_update(b)
a
{9, 10, 11}
b.intersection_update(a)
b
{9, 10, 11}
#symmetric_difference_update()
a={10,20,30,40,50}
b={30,40,50,60,70}
a.symmetric_difference_update(b)
a
{20, 70, 10, 60}
b.symmetric_difference_update(a)
a
{20, 70, 10, 60}
#pop and remove(0
a={2,3,4,5,6,7}
a.pop()
2
a
{3, 4, 5, 6, 7}
>>> a.remove(5)
>>> a
{3, 4, 6, 7}
>>> a.discard(3)
>>> a
{4, 6, 7}
>>> a={5,6,7,8,9,10}
>>> a.copy()
{5, 6, 7, 8, 9, 10}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add{60}
SyntaxError: invalid syntax
>>> b.add()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    b.add()
TypeError: set.add() takes exactly one argument (0 given)
>>> b.add(60)
>>> b
{60}
>>> #isdisjoint()
>>> a={4,5,6,7,8}
>>> b={9,10,11,12,}
>>> a.isdisjoint(b)
True
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> a.count(4)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.count(4)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(6)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.index(6)
AttributeError: 'set' object has no attribute 'index'
