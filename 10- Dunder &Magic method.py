'''
x = [1,2,3]
y = [4,5]

print(x+y)
print(len(x))
print(x[1])

#why is it that we can use these methods on lists ?
#There is something under the hood that tels python what to do


Dunder method = Data modeling method....  __def__()
'''


class Person :
    def __init__(self,name):
        self.name = name

    def __repr__(self): #what to do when you print the instance of object
        return f"My name is {self.name}"

    def __mul__(self,x):
        if type(x) is not int :
            raise Exception("Invalid argument ,must be int ")
        
        self.name = self.name * x


    def __call__(self,y):
        print("We called :",y)

    def __len__(self):
        return(len(self.name))
        

    


p = Person('Tim')
print(p) #it will print the memory address not the name

#print {self.name} * 5
p*5
print(p)

#call method
p(4)

#len method
print(len(p)) #it will print 15 : len(p)*5 = 3*5 = 15

print('............................................................')


from queue import Queue as q
import inspect


"""
print(inspect.getsource(Queue)) #if you wanna get the sourcecode of a datastructure
"""

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self,item):
        self.put(item)

    def __sub__(self ,item):
        self.get()



qu = Queue()
print(qu)

qu + 9
qu + 7
qu - 13

print(qu)
















    


