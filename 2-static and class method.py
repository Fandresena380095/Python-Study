class Person(object):

    population = 50
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod #you don't have to have an object of the class,you just need the class
    def getPopulation(cls):
        return cls.population

    @staticmethod #it is an independant function within the class that doesn't need any parameter
    def isAdult(age):
        return age >= 18
        #static method doesn't have acces to the class name ,so
        #can't use the parameters predefined in the class

    def display(self): #it is a regular method
        print(self.name, 'is', self.age, 'years old')



#simple method on an object of the class
newPerson = Person("Tim" ,18)
newPerson.display()

#use of the classmethod
print(Person.getPopulation())

#use of static method
print(Person.isAdult(17))
print(Person.isAdult(newPerson.age))
