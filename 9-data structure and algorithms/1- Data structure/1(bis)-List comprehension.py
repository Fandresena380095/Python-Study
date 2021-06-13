'''
There are simplier way to create a list 
'''


li = [it for it in range(10)]
#or
sqr_li_odd = [x**2 for x in range(11) if x%2==0]
print(sqr_li_odd)

# odd numbers _ you don't have to use a range;;;
#you can use a list
li2 = [x for x in range(11) if x%2==1 ]
print(li2)

#get multiple of 10:
print([x*10 for x in li2 ])


#get numbers from string : .isnumeric()
s = "I 9 am pleased to 23 be here"
nums = [x for x in s if x.isnumeric()]
print(nums)

#using __enumerate(list)__: to look for INDEX or VALUE
names = ['Pedro','Jani','Klauss','Berzeck']
print([index for index,value in enumerate(names) if value == 'Klauss'])

#use random method
import random

letters = [x for x in 'ABCDEF']
random.shuffle(letters)
print(letters)

#remove some of the list's content
letrs = [u for u in letters if u!= 'C']
print(letrs)


















