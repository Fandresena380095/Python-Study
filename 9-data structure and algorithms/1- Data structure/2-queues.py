'''
It follows the FIFO method
(first in first out)


Enqueue:-End                             Dequeue:-Front

Item5 -------->Item4,Item3,Item2 ---------> Item1

You use it for pretty much anything:
    McDo call line , lines ,.......

-Python provides already a built in collection called deque

'''
"""
from collections import deque as d

queue1 = d()
queue1.append(2)
queue1.append(4)
queue1.append(3)
queue1.append(5)
print(queue1)
print(queue1.popleft()) #prints the value of the item removed
print(queue1) #prints the other values
"""

"""
Wrapped method
"""

class Queue(): 

    def __init__(self):
        from collections import deque #put it under the initialization function
        self.queue = deque()
        

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
        
    def get_size(self):
        return len(self.queue)
        

    def clear(self):
        return self.queue.clear()

    def __str__(self):
        return str(self.queue)


queue2 = Queue()
queue2.enqueue(1)
queue2.enqueue(2)
queue2.enqueue(3)
queue2.enqueue(4)
queue2.enqueue(5)
print(queue2)
print(queue2.dequeue()) #Print out the first item removed
print(queue2)
print(queue2.get_size())

        

    
















































    
