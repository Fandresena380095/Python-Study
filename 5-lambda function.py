#lambda = anonymous function
'''
This is a simple function
def func(x):
    return x+5

print(func(2))
'''
#another way to make it:
func = lambda x: x+ 5

print(func(2))

#multiple parameters
func3 = lambda x,y : x+y

print(func3(6,9))


#You can use them within functions()
def mainFunc(x):
    func2 = lambda x: x+5 #if you wanna do the same operation within functions
    return func2(x) + 85

print(mainFunc(2))

#You can use them within map() and filter()
print("A simple list")
a = [i for i in range(11)]
print(a)

print("When all the elements of a have been added with 5")
newList = list(map(func ,a))
print(newList)
            #OR#
newList2 = list(map(lambda x: x+5 ,a))
print(newList2)

print("New list where all the numbers of list1 are even")
newList3 = list(filter(lambda x: x%2==0 ,newList2))
print(newList3)




#let's say you wanna sort a hybrid list-dictionary by name/age/country 
students = [
    {"name":"John" ,"age":18 ,"country":"USA" },
    {"name":"Alex" ,"age":20 ,"country":"Canada" },
    {"name":"Zack" ,"age":21 ,"country":"Australia" },
    {"name":"Brian" ,"age":24 ,"country":"South Africa" }
]

#you can sort a name by using
def sort_function(person):
    return person["name"]  #returns the value of the key "name"

students.sort(key = sort_function)
print(students)

#or simply
students.sort(key = lambda person : person["age"])
print(students)

