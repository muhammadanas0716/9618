# DECLARE StackData : ARRAY[0:9] OF INTEGER
# DECLARE StackPointer : ARRAY[0:9] OF INTEGER

global StackData
global StackPointer
StackData = [0 for i in range(10)]
StackPointer = 0

def PrintArray():
    print(StackPointer)
    for x in range (0, 10):
        print(StackData[x])


def Push(value: int):
    global StackPointer, StackData

    if StackPointer == 10:
        return False

    StackData[StackPointer] = value
    StackPointer += 1
    return True


counts = 0
while counts != 11:
    value = int(input("Enter a number: "))
    temp = Push(value=value)
    if temp == True:
        print(f"Added {value} to stack")
    else:
        print(f"Was not able to add to stack. Stack is full.")

    counts += 1


PrintArray()

def Pop():
    global StackPointer, StackData

    if StackPointer == 0:
        return False

    StackPointer -= 1
    return StackData[StackPointer]

Pop()
Pop()

print(f"Stack Pointer is {StackPointer}")


# 25 / 25 