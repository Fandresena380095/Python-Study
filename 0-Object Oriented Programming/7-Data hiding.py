#Data hiding
'''
We use __ to hide values

'''
class MyClass:

    #hidden member of the class
    __hiddenVariable = 50

    #A method that uses increment and the hidden variable
    def add(self,increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)

myObject = MyClass()
myObject.add(2) #>52
myObject.add(9) #>61 (52 + 9)

#This will print error:
'''
print(myObject.__hiddenVariable)
'''
#To acces the value of the hidden variable,we use:
#instance._className__hiddenValue
print(myObject._MyClass__hiddenVariable)


print("....................................................")





















    
