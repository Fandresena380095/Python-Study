data = [2,3,5,8,9,12,39,43,99,102,104]

'''
#if you have to look for an element in a list ,you would
#think first of this method :
def linear_search(target):
    for i in range(len(data)): #it will go through the database one by one
        if data[i] == target:
            return True
    return False
'''

"""
It is essential to have a SORTED LIST....
We are going to split the list in half ,and ask if the target is
    greater or smaller than the middle value ,,,
    #Binary search will save you a lot of time
"""


def binary_search_iterative (data ,target):
    low = 0 #index of the first element
    high = len(data) -1 #index of the last element of the list

    while low <= high : #while the list exists > recursive loop
        mid = (low + high) // 2 #index of the middle element
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1 #the index of the highest in the list will break in half
        else:
            low = mid + 1
    return False

print(binary_search_iterative(data ,104))


def binary_search_recursive(data ,target, low,high):
    if low > high :
        return False
    else :
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data ,target ,low, mid -1)
        else :
            return binary_search_recursive(data ,target ,mid +1, high)

print(binary_search_recursive(data,102,0,len(data)-1))
            
    

































            
        
