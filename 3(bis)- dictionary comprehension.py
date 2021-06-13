tick = {
    "Dave" : 23 ,
    "John" : 20 ,
    "Durk" : 26 ,
    "Dako" : 29 ,
    "Jill" : 20 ,
    "Jeanette" : 17 ,
    "Jane" : 15 ,
    "Julia" : 29 ,
    "Jake" : 12 ,
    "Jakob" : 15 ,
    "Jason" : 15 ,
    "Jared" : 25 ,
    }
#simple example:
print("Simple example of creating a new dictionary")
numbers = {i:str(i) for i in range(len(tick))}
print(numbers)


#Print all the items in the dictionary ( .items()):
print("printing all the items in a dictionary")
print({(k):(v*2) for (k,v) in tick.items()})


#Create a dictionary of all the adults/teens of the list:
adults = {k:v for k,v in tick.items() if v>=18}
print(adults)
print("number of adults : ",len(adults))

teens = {k:v for k,v in tick.items() if v<18}
print(teens)
print("number of teens : ",len(teens))

#advanced features if/else key/value:

                    #key iteration#
print({(k if k=='Dave' else 'Jane'):v for k,v in tick.items()})
                    #value iteration#
adult_teen_sep ={k:('adult' if v>=18 else 'teen') for k,v in tick.items()}
print(adult_teen_sep)



#USEFUL function .zip()
names = ['Jake','Joe','James','Jude','Jackob','Jules']
ages = [14,15,13,19,21,13]
total = dict(zip(names ,ages))
print(total)
