'''
    1-so like building a house ,we need :

[brick,wood,windows,...] + home building instruction ==> House

so does a software application :

[linked list,trees,arrays....] + algorithm ==> Application

.............................................................................

    2-You need to use the rigth data structure to solve a problem .So you have
to have the clear understanding of what a data structure is.

.............................................................................

    3-for example :
    -you make an app for apple's stock price for 5 days:
a. What was the price for day 1 ?
b. What was the price for day 3 ?

                    use a list :
                    
stock_price = [223,225,230,229,227]

day_1 = stock_price[0]
day_3 = stock_price[3]

    -but what if you wanna store the price along with the dates ? from march4
march7
a. What was the price on march4 ?
b. What was the price on march7 ?

                    use a dictionary :

stock_price = {
            'march 4' : 223,
            'march 5' : 225,
            'march 6' : 230,
            'march 7' : 229
}

march_4 = stock_price['march 4']
march_7 = stock_price['march 7']

.............................................................................
    4-there two methods are processed differently


'''




'''
BIG O NOTATION
    it is used to measure how the running time and the space requirement for your
program grows as input size grows
    as the size grows ,the time will also grow


1- A linear complex program is written O(n), if you have 10000 iterations,
the execution is going to run 10000 times
[(D) = an + b]
     example :
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in squared_numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers = [2,5,8,9]
get_saquared_numbers(numbers)
#returns [4,25,64,81]

2- A constant function is written O(1)
time is constant
        example:
def find_first_pe(prices ,eps, index):
        pe = prices[index]/eps[index]
        return pe

3- An n**2 program is going to be as the following: O(n**2)

numbers = [3,6,2,4,3,6,8,9]
                        """""to learn"""""
for i in range(len(numbers)):
    for j in range(i+1 ,len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i], "is a duplicate")
            break
#it takes i and j as arguments therefore it is a n**2 complex program
let's say you have a time equation :
    time = 5n^2 + 3n + 20
if n = 1000
you will have :
    time = 5000000 + 3020
    time = 5003020
'''
#EXAMPLE
'''
#>>>>>>>>>>>Always keep the fastest way to solve a problem:
#Let us try to sort a list using 2 methods:
                    #METHOD 1#
print('#METHOD 1#')

numbers = [545454,86754,545232,8098675,6465343,76,6565656,87876453,6565335,65656564,87,865]

for i in range(len(numbers)):
    for j in range(i+1 , len(numbers)):
        while numbers[i] > numbers[j]:
            numbers[i] ,numbers[j] = numbers[j] ,numbers[i]
        print(numbers)

                    #METHOD 2#
print(' ')
print('#METHOD 2#')
numbers.sort()
print(numbers)
'''





















        
        
        

































