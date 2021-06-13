#you will access elements by name using namedtuple()
import collections
from collections import namedtuple
#They will act as a new class 
#initializations 
Point = namedtuple('Point','x y z')
#You will get objects from your namedtuple() which allows you
#to use it as a class
newPoint = Point(3,4,5) #x=3 ,y=4, z=5
print(newPoint)
            #or#
    #       with ._make()
newPointNew = Point._make([3,4,5])
print(newPointNew)

print('...................................................')
#another example with a list:
PointSec = namedtuple('PointSec' ,['a','b','c'])
newPointSec = PointSec(4,3,8)
print(newPointSec)

#another example with a dictionary:
PointSec2 = namedtuple('PointSec2' ,{'a':8,'b':8,'c':8})
newPointSec2 = PointSec2(9,3,6)
print(newPointSec2)
print('.......................................................')


#you can acces every element by its name:
print(newPointSec2.a ,newPointSec2.b ,newPointSec2.c)
print(newPointSec2[0])

#you can transform it as a dictionary with ._asdict():
print(newPointSec2._asdict())
#you can see the keys with ._fields:
print(newPointSec2._fields)

print("...................................................")
#you can replace with ._replace():
#mandatory to create another object before using ._replace
P = newPointSec2._replace(a=32)
print(P)



































