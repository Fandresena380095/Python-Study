
class Dog(object):
    def __init__(self, name,age):#this needs to be here,whenever you create an object of the class Dog,this will automaticaly fire
        self.name = name
        self.age = age
        self.li = [1,3,5]

    def bark(self): #bark would be a method of the class Dog
        print(f"Ouf!Ouf!Hi ,I am {self.name} and I am {self.age} yo")


    def change_age(self , age):
        self.age = age

    
#----------°°°°+°°°°----------:
    def add_weight(self,weight):
        self.weight = weight

'''
if you put a parameter in init, you have to use
a parameter when you create the object of the class you
created
'''

Tim = Dog("Tim",7) #Tim is the object that is passed in the parameter self
Tim.bark()

Tim.change_age(10)
Tim.bark()


#You can also acces to the attributes of your ojects directly
print(Tim.age)
print(Tim.name)
print(Tim.li)


#----------°°°°+°°°°----------:
Tim.add_weight(20)
print(Tim.weight)


'''
WHY CREATING YOUR OWN CLASS?

if you wanna perform a method for 10000 objects ,
you need to shorten your code

'''
