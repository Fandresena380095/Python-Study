import collections
from collections import Counter

c = Counter('gallad')
print(c)
e = Counter(['a','a','b','c','c','c'])
print(e)
y = Counter({'a':1, 'b':2})
print(y)
t = Counter(cats =4 ,dogs =7)
print(t)
print(t['cats'])
print(t['pets']) #it will just return 0


#you can make a dictionary (.items()) out of the counter  method:
print(dict(c.items()))

#you can make a list ( .elements()) out of it:
print(list(c.elements()))

#you can also use .most_common(number) method to define which one is the most common:
print(e.most_common(1)) #you will get a list with a value
print(e.most_common(2))
print(e.most_common(3))

print('..........................................................')
            #another useful method#
x = Counter(a=4 ,b=2, c=0, d=-2)
y = ['a','b','b','c']

# .subtract :
x.subtract(y) #we subtracted the elements of x by y
print(x)

# .update: (add)
x.update(y)
print(x)

# .clear:
x.clear()
print(x)
print('.....................................................................')

            #other methods#
p = Counter(a=4 ,b=2, c=0, d=-2)
q = Counter(['a','b','b','c'])

print(p+q)
print(p-q) #if the element is <=0 it won't show in the counter
print('....................................................................')
print('p :',p ,'q :',q)
print(p & q) #intersectioon
print(p | q) #union
print(q - p) #in q not in p
print(p - q) #in p not in q




























