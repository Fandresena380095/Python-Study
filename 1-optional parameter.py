#it is a value that you already in the parameter
'''
def func(x=1):
    return x**2

call =func()
print(call)

call2 = func(5)
print(call2)

#but more useful use:
def energy(mass ,celerity=8000):
    return mass * (celerity**2)

atom1 = energy(28)
print(atom1)


#multiple parameter
def energy_conversion(p,gravity=10 ,celerity=8000):
    return p*gravity*(celerity**2)

atomP1 = energy_conversion(2.8)
print(atomP1)

atomP2 = energy_conversion(2.7 ,10,8100)
print(atomP2)

'''

#real life example:
class Car:
    def __init__(self, make, model, year , condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self ,showAll):
        if showAll : #means if showAll is true
            print("This car is a %s %s from %s, it is %s and has %s kms." %(self.make,self.model,self.year,self.condition,self.kms))
        else :
            print("This car is a %s %s from %s." %(self.make ,self.model, self.year))


speedy = Car('Volkswagen' ,'type4',2009, 'good' ,25000)
speedy.display(True)
speedy.display(False)

#But what if we have a new car with by default 0kms :

class New_Car:
    def __init__(self, make, model, year , condition ='new', kms = 0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self ,showAll):
        if showAll : #means if showAll is true
            print("This car is a %s %s from %s, it is %s and has %s kms." %(self.make,self.model,self.year,self.condition,self.kms))
        else :
            print("This car is a %s %s from %s." %(self.make ,self.model, self.year))

golfy = New_Car('Volkswagen' ,"type2" , 2021)
golfy.display(True)
golfy.display(False)



























        



















