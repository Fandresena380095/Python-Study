class _Private: #they can be accessed in a certain file
    def __init__(self ,name):
        self.name = name


class NotPrivate: 
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self): #Private method
        print("Hello")

    def display(self): #Public method
        print("Hi")


#the underscore _ is just a convension between Python programmers.
        #it is just used when you don't want people to use your class
        #but it is still usable anytime by everyone
