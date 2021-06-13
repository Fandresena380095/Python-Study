
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self): 
        print("Ouf!Ouf!Hi ,I am" , self.name,"and I am", self.age , "yo")

    def aggressiveDog(self):
        print("OUUUUFFF!!!!!")


"""
#instead of copying the same class as Dog like this:

class Cat(object):
    def __init__(self, name, age,color):
        self.name = name
        self.age = age
        self.color = color

    def miaou(self): 
        print("Ouf!Ouf!Hi ,I am" , self.name,"and I am", self.age , "yo")


#do :
class Cat(Dog):
#Dog : Parent class
#Cat : Child class
"""

"""
When you inherit a class() from another class() ,you can use ALL THE METHOD
of the class Parent to the class Children

________________________________this is how it works :

def childClass(parentClass):
    #initialisation :
     ....

     #method:
"""

class Cat(Dog):
    def __init__(self, name , age , color):
        super().__init__(name, age) #this syntax initialize the atribute name and age to the childClass ,you don't have to type self.name = name ... anymore
        self.color = color #new parameter that still need to be initialized

#you can override a method in a parent's class
    def aggresiveDog(self):
        print("Miaouuuuuuu!!!")





#Dog using a Parent's class:
Tom = Dog("Tom" ,23)
Tom.aggressiveDog()

#Cat using a modified class:
Ron = Cat('Ron' , 13, 'grey')
Ron.bark()
Ron.aggresiveDog()



'''When do you wanna inherit ?'''
"""
When you wanna create a general class ,then some modifications
of the original class
example : class vehicle can be a car, boat , train ....and each vehicle
has common methods, and specific methods

"""

#General vehicle class
class Vehicle():
    def __init__(self,price,gas,color):
        self.price = price
        self.gas = gas
        self.color = color

    def empyTank(self):
        self.gas = 0

    def fullTank(self):
        self.gas = 1000

    def gasLeft(self):
        return self.gas


        
#specific class = Car
class Car(Vehicle):
    def __init__(self,price,gas,color,power):
        super().__init__(price ,gas,color)
        self.power = power

    def horn(self):
        print("beep beep")

    def powerLevel(self):
        self.power += 36 #this will add 36 to the original power
        print(self.power)


merced = Car(2000,1001,'blue',3000)
merced.powerLevel() #it will print 2000 bc it is self.power is already defined as 2000
merced.horn()


#another specific class = Boat
class Boat(Vehicle):
    def __init__(self,price,gas,color,position):
        super().__init__(price,gas,color)
        self.position = position

    def hornBoat(self):
        print("DRIIIIIIINNNNNNN")

cruisade = Boat(32000,1001,'silver',-2367327676467674)
print(cruisade.position)
cruisade.hornBoat()


