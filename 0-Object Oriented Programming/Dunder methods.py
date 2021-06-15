#printing methods are primordial: __repr__    __str__

class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a:%s b:%s" %(self.a ,self.b)

    #or
    def __str__(self):
        return "From str method of Test: a is %s ,"  \
               "b is %s" %(self.a ,self.b)


st = Test(123,126)
print(st) #will print the __str__ method
print([st]) #will print the __repr__ method
print(' ')

#IF THERE IS NO __STR__ METHOD , PRINT(T) USES REPR
class Test2:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a:%s b:%s" %(self.a ,self.b)

st2 = Test2(199,190)
print(st2)
print(' ')

#IF THERE IS NO __REPR__ METHOD ,PRINT(T)  WILL GIVE YOU AN ADDRESS
class Test3:
    def __init__(self,a,b):
        self.a = a
        self.b = b


st3 = Test3(199,190)
print(st3)
