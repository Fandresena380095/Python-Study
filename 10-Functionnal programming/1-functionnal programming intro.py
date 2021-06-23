'''
It is a paradigm in which we try to bind everything in pure mathematical
function style

The main focus is WHAT TO SOLVE (in contrast to HOW TO SOLVE)

It uses expression instead of statements 
'''

#Pure functions : doesn't change the input list 
def pure_func(list):
    New_List = []

    for i in list :
        New_List.append(i**2)

    return New_List

Original_List = [1,2,3,4]
Modified_List = pure_func(Original_List)

print(Original_List)
print(Modified_List)

print("....................................................................................")

#Recursive functions : call itself ,needs a base

def sum(L,i,n,count):
    #base
    if n <= i:
        return count

    count += L[i]

    count = sum(L,i+1,n,count)
    return count

L = [1,2,3,4,5]
count = 0
n = len(L)
print(sum(L,0,n,count))

print("..................................................................................................")

#Functions are first class and can be high class:
        #A function is an instance of an object type 
        #You can store function in a variable
        #You can pass the function as a parameter to another function
        #You can store them in data structures......lists....

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    #storing a function in a variable
    greeting = func("Hi I am glad to be here with you now....")
    print(greeting)

greet(shout)
greet(whisper)

print("....................................................................")

#map() & filter() :
                #map():
def sqrt(n):
    return n**(1/2)

numbers = [1,4,9,16,25,36]

squareroots = map(sqrt ,numbers)
#No values yet
print(squareroots)
#values in a float form (use int() to transform them)
for i in squareroots:
    print(int(i), end = " ")
print(" ")
                #filter(): based on booleans logic

def voyelles(v):
    voy = ['a','e','i','o','u']

    if v in voy:
        return True
    else:
        return False


text = 'I am very pleased to be here'
count_voy = filter(voyelles ,text)

for i in count_voy:
    print(i)
    
num_voy = len(list(filter(voyelles,text)))
print(num_voy)

print(".......................................................")

#lambda
            #can be used as an instance of an object
            #independant functions

cube = lambda x: x**3
print(cube(6))

#list comprehensions
numbers = [i for i in range(11)]
even_numbers = [x for x in numbers if x%2==0]
print(numbers)
print(even_numbers)




























    





















    
