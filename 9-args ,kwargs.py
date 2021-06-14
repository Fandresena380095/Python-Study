#Args ,kwargs ,functional arguments*


#When you do not know how many arguments will be passed in
#a function ,we use *Args

def print_num(*num):
    print(num)

print_num(1,2,3,4,5)

#use the sum() keyword to perform an addition
def add(*num):
    print(sum(num))

add(1,2,3,4,5,6)

print(".................................................................")
#another keyword argument and default arguments
def presentation(name,age,place = "Madagascar"):
    print("I am",name)
    print("and I'm getting",age ,"years old")
    print("And I live in",place)

presentation("Luke",22)
print("..............................................................")
#**Kwargs are used when you don't know how many keyword argument
#are going to be passed on
#it will return a dictionary

def user(**username):
    print(username)

user(username1= "XYZ" ,username2 = "ABC")

            #you can acces the value directly by it's keyword
def user2(**user_detail):
    print("Name :",user_detail['username'])
    print("Age :",user_detail['age'])
    print("Address :",user_detail['address'])

user2(username= "Marco" ,age=22 ,address = "23,Rue J.C ,France")





































