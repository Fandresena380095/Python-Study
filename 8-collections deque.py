import collections
from collections import deque

#why using deque ?
#it is faster to work adding a element at the end/beginning of a list
#easier modules of stacks(LIFO) and queues(FIFO)

d = deque('hello')
print("ORIGINAL :")
print(d)

d.append(4)
print("ADD 4 AT THE END OF THE LIST")
print(d)

print("ADD 6 AT THE BEGINNING OF THE LIST")
d.appendleft(6)
print(d)

#you can remove an element at the end:
d.pop()
print(d)

#as well as at the beginning
d.popleft()
print(d)

print('..................................................................')
#remove allthings:
d.clear()

d.extend('456') #it will add 456 as a list
print(d)

d.extend('hello')
print(d)

d.extendleft('123') #(LIFO)
print(d)

print('..............................................................')
#we can also use .rotate(number)
d.rotate(-1) #this will make the 2nd element the first:
            #2nd -> 1rst ,3rd -> 2nd,...
print(d)

d.rotate(3)
print(d)

print("..........................................................")
#maxlen attribute on deque:
a = deque("Happy" , maxlen  = 5)
print(a)
a.append(78) #ti will remove the first element
print(a)
a.appendleft('H')
print(a)
a.extend([1,2,3])
print(a)
a.extendleft('paH') #reveerse method for stack (LIFO)
print(a)
a.reverse()
print(a)

















              
