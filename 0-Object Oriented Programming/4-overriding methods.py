'''
    If you ever wondered , how does Python add, substract , or multiply
2 objects of the same class ,,,,
    There are methods that you can use to make it work 

'''
class Point():
    def __init__(self , x=0, y=0): # (0,0) are the initial value of the Class
        self.x = x
        self.y = y

#MANDATORY METHOD FOR PRINTING THE COODRINATES,not the adress: #"self" refers to the instance of the class
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
        # ===> (x,y)
        # You can use any syntax you want , but the String value is necessary



#OPERATION METHODS :

    def __add__(self ,p):
        return Point(self.x + p.x ,self.y + p.y)
    #for example p1 + p2
    #p1 will take the (self )init = self coordinates (self.x ,self.y)
    #p2 will take the (p )init = p coordinates (p.x , p.y)
    #it will return a new point witch has the coordinates of p1 + p2

    def __sub__(self ,p):
        return Point(self.x - p.x ,self.y - p.y)

    def __mul__(self ,p):
        return self.x * p.x + self.y* p.y
    #this is a scalar product of a vector:
    #for two points A(x,y) and A'(x',y'):
    #                A.A' = x.x' + y.y'

#COMPARISON METHODS :
    #import a geometric length method (argument A(x,y)= sqrt(x^2 + y^2))
    def argument(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

  
    def __gt__(self,p):  
        return self.argument() > p.argument()

    def __ge__(self,p):  
        return self.argument() < p.argument()
    
    def __lt__(self,p):  
        return self.argument() >= p.argument()
    
    def __le__(self,p):  
        return self.argument() <= p.argument()
    
    def __eq__(self,p):  
        return self.x == p.x and self.y == p.y




p1 = Point(3 ,4 )
p2 = Point(3 ,2 )
p3 = Point(1 ,3 )
p4 = Point(0 ,1 )

print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)



