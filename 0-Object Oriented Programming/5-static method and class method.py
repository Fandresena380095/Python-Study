'''
regular methods need the instance(self) as an argument
instance = object (self)

how can we change this if we wanna use the class as an argument?
use a @classmethod
'''


class Dog():

#These are variables within you class,you can create them without initializing them 
    dogs = []
    
    def __init__(self ,name):
        self.name = name
        self.dogs.append(name) #You are appending every dog object of the class Dog in the list dogs you created

    @classmethod #They are used if you wanna access to a class variable (dogs) without having to use an object of the class
    def num_dogs(cls): #cls is a reference to the actual class?so that you could use the method directly on the class
        return len(cls.dogs)

    @staticmethod #They are used if you wanna create an independant function within the class...
    def bark(n):
        '''barks n times'''
        for _ in range(n):
            print("BARK!")



            
"""
example of static method:
class Maths():
    @staticmethod
    def add(x,y):
        return x + y

print(Maths.add(4 , 9))
"""

   
Tim = Dog("Tim")
Jim = Dog("Jim")
Tom = Dog("Tom")
Jen = Dog("Jen")
Tius = Dog("Tius")

#classmethod are used if you do not wanna reference an instance of an object:
print(" Print the list dogs of the class Dog : ")
print(Dog.dogs)


print("When you use the class method on Dog : ")
print(Dog.num_dogs())



#static method: they are independant function that are within a class
#They are mostly used within an import module
Dog.bark(5)


