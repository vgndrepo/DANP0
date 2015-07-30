'''
Created on Jul 28, 2015

@author: VGHANTA
'''

def hello(myInput):
    return "hello world: "+myInput

def fizzbuzz(intList):
    updateList = []
    
    for i in intList:
        if i%3 ==0 and i%5 ==0:
            updateList.append("FizzBuzz")
        elif i%3 == 0:
            updateList.append("Fizz")
        elif i%5 == 0:
            updateList.append("Buzz")
        else: 
            updateList.append(i)
    return updateList    

print("hello world")
outList = fizzbuzz([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print(len(outList))

for j in outList:
    print(j)
