# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:42:34 2024

@author: maxdu
"""
import time

#Passed Boundary
#Passed Idempotency Cases
def partitionArray(array, low, high):
    
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:

        pi = partitionArray(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)

#Enter your data here.
dataInput = []

#Negative Case
def negativeTest(negData):
    print("Negative Data:")
    if isinstance(negData, list):
        print("Input data in array format")
        for i in range(len(negData)):
            if isinstance(negData[i], int):
                print("Input data children are in correct format at ", i)
            else:
                print("Input data children are not in correct format")
                break
    else:
        print("Input is not an array")
        
negativeTest(dataInput)

#Performance Case
def performanceTest():
    timeTaken = endTime - startTime
    print("Time Taken: {} seconds".format(timeTaken))

startTime = time.time()
print("Unsorted Array")
print(dataInput)

#Positive Case
size = len(dataInput)
quickSort(dataInput, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(dataInput)
endTime = time.time()
performanceTest()