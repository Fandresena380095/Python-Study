'''
1- stack is a LIFO data structure
(Last In First Out)

Item4
    |
    | Push()
    |
    v
|          |
| Item3    |
| Item2    |
| Item1    |
|__________|                      



Item4
    A
    | Pop()
    |
    |
|          |
| Item3    |
| Item2    |
| Item1    |
|__________|


The only way to acces Item1 is to remove all the Items before it
        other functions are:
Peek() = Get acces to the item on the very top

Clear() = Remove all the items



-------------------------------------------------------------------------
There are a lot of way to use it:
- Keep record of your commands for undoing whatever you messed up
- You can use the .append() and .pop() method to simulate a stack
'''

class Stack():
    def __init__(self):
        self.stack = list()

    def push(self,item):
        self.stack.append(item) #list.append

    def pop(self):
        if len(self.stack) > 0: #check if the list is empty
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def clear(self):
        return self.stack.clear()

    def __str__(self):
        return str(self.stack)


sta1 = Stack()
sta1.push(1)
sta1.push(2)
sta1.push(3)
sta1.push(4)
sta1.push(5)
print(sta1)
print(sta1.pop()) #Print the item taken
print(sta1)
print(sta1.peek())






























