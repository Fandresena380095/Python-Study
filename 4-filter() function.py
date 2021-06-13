def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0 #filter() is based on True/False logic

#list comprehension
a = [i for i in range(11)]
print('a = ',a)

b = list(filter(isOdd ,a)) #based on booleans logic : True/False 
                            #whatever is False won't be appended to b
print('b = ',b)

c = list(map(add7 ,b))
print('c = ',c)
#or :
d = list(map(add7 ,(filter(isOdd ,a))))
print('d = c =',d)



