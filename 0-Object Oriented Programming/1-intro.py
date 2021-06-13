'''

______________An object is pretty much everything:______________
x = 23
y = 'string'

x is an object of the class int()
y is an object of the class string()

-- we will have built in method for each class --
-- these class had already been created by people --

______________type on the Python shell___________________
>>> help(int)
if you want to know how the class int() is written

__________________________FUNCTION VS METHOD_____________
1_FUNCTION:
def func(x):
    ...arg...

print(func(8))


2_METHOD:
x = "lol"

print(x.upper())

'''

#call a method: variable.method()

y = " Guy is weird ,Guy doesn't like people"

print(y.replace('Guy', 'Donald Trump'))

#call a function: function(variable)

z = " Guy is weird ,Guy doesn't like people"
def rep(x):
    x = x.replace('Guy' , 'Donald Trump') #ja,method in a function
    return x

print(True + False)
print(rep(z))
    
