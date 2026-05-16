arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8] 

def linearSearch(searchValue):
    for x in range(0, 10):
        if arrayData[x] == searchValue:
            return True
        
    return False


# number = int(input("Enter your number: "))
# functionCallResult = linearSearch(number)
# if functionCallResult == True:
#     print("Found.")
# else:
#     print("Not found.")


def bubbleSort():
    temp = 0
    n = len(arrayData)

    for i in range(n-1):

        for j in range(n - 1 - i):
            if arrayData[j] < arrayData[j + 1]:
                temp = arrayData[j]
                arrayData[j] = arrayData[j + 1]
                arrayData[j + 1] = temp

    return arrayData

print(bubbleSort())


# 20 / 20


