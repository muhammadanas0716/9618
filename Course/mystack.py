Stack = [""] * 5

# Pointer who will control the data (Push/Pop) - LAST IN FIRST OUT
Pointer = 0


def Push(value):
    global Stack
    global Pointer

    if Pointer == len(Stack):
        return False
    else:
        Stack[Pointer] = value
        Pointer += 1
        return True


def Pop():
    global Stack
    global Pointer

    if Pointer == 0:
        return "Nothing to pop. Empty"

    else:
        Pointer -= 1
        return Stack[Pointer]


# OOP VERSION
class StackOOP:
    def __init__(self, size):
        self.__stack = [""] * size
        self.__pointer = 0

    def push(self, value):
        if self.__pointer == len(self.__stack):
            return False

        self.__stack[self.__pointer] = value
        self.__pointer += 1
        return True

    def pop(self):
        if self.__pointer == 0:
            return None

        self.__pointer -= 1
        return self.__stack[self.__pointer]
