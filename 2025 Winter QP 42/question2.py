import random

# DECLARE RandomArray : ARRAY[0:19] OF INTEGER
RandomArray = [random.randint(0, 100) for i in range(20)]

def PrintArray(IntegerArray):
    for i in IntegerArray:
        print(f"{i}", end=" ")

# PrintArray(RandomArray)

def BubbleSort(IntegerArray):
    n = len(IntegerArray)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if IntegerArray[j+1] < IntegerArray[j]:
                IntegerArray[j+1], IntegerArray[j] = IntegerArray[j], IntegerArray[j+1]

    return IntegerArray

PrintArray(BubbleSort(RandomArray))

def RecursiveBinarySearch(IntegerArray, LowerBound, UpperBound, ValtoFind):
    pass

# 17 / 26