#it will allow you to apply a function in a list
#and create another list out of it 

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x
'''
#try to apply the function fun(x) to the list ??
#you will probably do the following

newList = []
for x in li :
    newList.append(func(x))

print(newList)
'''
#instead you can do the following: list(map(function,*iterable))
print(list(map(func ,li)))

#or you can do a LIST COMPREHENSION:
print([func(x) for x in li])
print([func(x) for x in li if x%3 == 0])

a = [i for i in range(11) if i%2==0]
print(a)
#print x belonging to the list a if x>=6
print([x for x in a if x>=6])




















