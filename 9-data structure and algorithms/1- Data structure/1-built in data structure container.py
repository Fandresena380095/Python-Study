#There are generaly 5 types of data structuring :


                            #1-STRINGS :

print("STRING")
a = "This IS a string"

#indexing :accessing any item by its index/and use index to slice them
print(a[3:12:2]) #[12] non included : [inclusife beginning:non_inclusive end:step]
print(a[-6])
print(a[3:])
print(a[:6])
print(a[-3:])
print(a[:-2])

#verifying
for t in a: #print 1 by 1 all the element in a
    print(t)

if "string" in a: #verify if "string" is in a
    print("Yebo")

#operations : concatenationg 
print(a+' '+a)
print(a*3)

#methods
print(a.upper())
print(a.lower())
print(a.count("i"))
print(a.replace("string", "cake"))
print(len(a))


print("...........................................................................................................................")

                            #2-LIST :
"""
- Generale purpose
- Sortable
- Used for almost everything
- Versatile and iterable

"""
print("LIST")
names = ["James", "Joe" , "Jude" , "Jack" ,"Jamie"]
matrx = [
        [1,2,3,4,5] ,
        [6,7,8,9,10]
        ]
x = [1,2,3,4,5,6,7,8,9,10]

#USING INDEX
print(names[2:-1])# [-1] non included
print(matrx[1][3]) #index 3 of the index 1 in matrx
print("index of Joe :",names.index("Joe"))


# V E R I F I C A T I O N
print("Joe" in names) #True / False
print("Jules" not in names)

#loops
for le in names: #prints all elements in names
    print(le)
if "Joe" in names:
    print("Yebo ,Joe is in it")
else :
    print("Nein")

#  M  E  T  H  O  D  S
print("number of Jude in names :",names.count("Jude"))
x.append(145)
x.remove(1)
x.insert(2,34)  #insert(index,value)
print(x)
print(x.count(2))
print(len(x))

#sum of all elements in a list :they have to be int or float
print(sum(x))
print(sum(x[1:]))

x.extend([9,67,99])
print(x)

x.reverse()
print(x)

x.sort()
x.sort(reverse=True)
# or
# sorted(x)
print(x)
print(min(x))
print(max(x))

#COMPREHENSION : creating easily a list by functions
square = [i*2 for i in range(10+1)] #append all multiple of 2 in a range of 0 to 11(non included) in square
print(square)

evens = [i**2 for i in range(11) if i**2%2==0]  #append all the **2 of even numbers in a rane of 0 and 11(non included) in evens
print(evens)

#Get the index and the item at the same time : enumerate function 
x = [23,36,99,320]
for index,item in enumerate(x):
    print(index,item)

#valid in a string,list,tuple: min / max >They have to be the same type
print(min(x))

y = ['Procrastination','Good','Nope','Carrer','Lie','Ir','am']
print(max(y)) #alphabetically max
print(min(y)) #alphabetically min
print(sorted(y, key=lambda k: k[1])) #this will sort y according to the 2nd letter


#UNPACKING: #you must have the same number of item as in the list
a,b,c,d = x
print(a,b,c,d)
#use *var to increment all the values to *var
a,*b = x
print(a)
print(b)

#You can use tuple to create a list:
a = (20,32)
b = list(a)
    
print("...........................................................................................................................")


        
                            #3-DICTIONARY :

'''
- Unordered
- Key/Value pair
- Associative array (HashMap (Java)) : k1 ----> v1
                                       k2 ----> v2
'''
print("DICTIONARY")
ages = {
    "Dave" : 20,
    "Xan" : 25,
    "John" : 22
}
agesD = dict(Dave=20 ,Xan=25, John=22)
print(agesD)

#Accessing values:
print(agesD.keys())
print(agesD.values())
print(agesD.items()) #both k/v

#using keys to show values
print(ages["Xan"])
print('?????????????????????????????')
for key in agesD:
    print(key  ,agesD[key])
print("?N?N?N??N?N?N?N?N")
for k,v in agesD.items():
    print(k,v)
print("?N?N?N??N?N?N?N?N")

#accessing values from keys
for i in ages:
    #define the variables for the values first
    valAge = ages[i]
    print(valAge)

#operation ,accessing the values of the dictionary
ages["Dave"] += 1
print(ages["Dave"])
# Update a dictionnary
ages["Jules"] = 28 
print(ages)


#verifying
print("Dave" in ages)
print(22 in ages.values())
print(22 in ages) #False ,there is no 22 key in ages
print("Jaiden" not in ages)

#the .get(key,value) method:if the key is not found,it will return the value given
                                    #if the key doesn't exist ,it will return the value given
print(ages.get("Xan"))
print(ages.get("Xan",26)) #it will still be 25 because Xan exists
print(ages.get("Hery" , "not found in the list"))

#the .pop() method:
ages.pop("Dave")
print(ages)





print("...........................................................................................................................")



                            #4-TUPLE :
'''
- They are immutable
- Faster than List
- Sequence functions
- They are used for fixed data
- If you have a list inside a tuple,you can change the list's data
'''

print("TUPLE")
#They are immutable
words = ("spam" , "eggs" , "sausages" , "beef" , "cheese")
nums = (1,(1,2,3,4),(6,67))
x = 2, # , is for creating a tuple
print(x,type(x))
x += 7, # do not forget the ","
print(x)

tup = ([6,4],2)
del(tup[0][1])
print(tup)


#This is a tuple addition :
y = ('yay','loop','good') + ('super',) #DO NOT FORGET THE COMA

#indexing
print(words[3])
print(nums[2])

#They can also be used as ------dictionnary keys------
origin = {
    ("Dave" , 20) : "Nigeria" ,
    ("Heritier" , 25) : "Congo"
}
print(origin[("Dave",20)])

#unpacking
numbers = (6,7,8)
a,b,c = numbers
print(a)
print(b)
print(c)

x,y = (1,2) #works with a list as well
x,y = y,x
print(y)
print(x)

#the *keyword is used to assing values
a,b, *c,d,e = range(20)
print(a,b)
print(c)
print(d,e)
print("...........................................................................................................................")


                            #5-SET :
'''
- They are useful to store unique values (non duplicated items)
- We can use math comparison operation on them (union ,...)
- They are faster than lists
- They are unordered
'''
#You can't duplicate a value in a set
print("SET")

nbr = {1,2,3,4,5,6,5,4,6,5,0}

li = [2,3,4]
x= set(li)
print(x)

#verifying
print(3 in nbr)

if 6 in nbr:
    print("Yes indeed")
else :
    print("Oh dear")
if 7 in nbr:
    print("Yes indeed")
else :
    print("Oh dear")

#O P E R A T I O N S : add() ,remove() ,len(set) ,pop a random item
print(nbr)
nbr.remove(6)
nbr.add(-45)
print(nbr)
print(nbr.pop(),nbr)

#set comparison
nbr1 = {1,2,3,4,5,6}
nbr2 = {4,5,6,7,8,9}
print("set comparison between nbr1: ",nbr1 ," and nbr2: ",nbr2)
print("                                ")
print("#all elements in nbr1 and nb2 + common ones ")
print(nbr1 | nbr2) 
print("#all elemens in nbr1 and nbr2 - common ones ")
print(nbr1 ^ nbr2) 
print("#all common elements in nbr1 and 2 ")
print(nbr1 & nbr2) 
print("#all elements in nbr1 not in nbr2 ")
print(nbr1 - nbr2) 
print("#all elements in nbr2 not in nbr1")
print(nbr2 - nbr1) 





    



