# DECLARE Stack: ARRAY[0:19] OF STRING
# DECLARE TopOfStack: INTEGER

global Stack, TopOfStack
Stack = ["-1" for i in range(20)]
TopOfStack = -1

def Push(value: str):
    global TopOfStack, Stack
    TopOfStack += 1

    if TopOfStack >= 20:
        TopOfStack = 19
        return -1
 
    Stack[TopOfStack] = value

    return 1

def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return "-1"

    temp = Stack[TopOfStack]
    TopOfStack -= 1

    return temp

def ReadData(fileName: str):
    try:
        fileToBeRead = open(fileName, "r")
        while True:
            line = fileToBeRead.readline().strip()
            if line == "":
                break
            else:
                temp = Push(line)
                if temp == -1:
                    print("Stack full")
                    break
        fileToBeRead.close()
    except IOError:
        print("File not able to load.")


ReadData("StackData.txt")

def Calculate():
    total = int(Pop())
    while TopOfStack != -1:
        operator = Pop()
        number = int(Pop())
        if operator == "+":
            total = total + number
        elif operator == "-":
            total = total - number
        elif operator == "/":
            total = total / number
        elif operator == "*":
            total = total * number
        elif operator == "^":
            total = total ** number
    
    return total

print(Calculate())
ReadData("SecondStack.txt")
print(Calculate())

# 25 / 27