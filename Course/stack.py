Bus = [""] * 5

# Pointer who will control the data (Push/Pop)
EmanBaja = 0


def Push(Value):
    global Bus
    global EmanBaja

    if EmanBaja > 4:
        print("Jaga nahi he bus me")
    else:
        Bus[EmanBaja] = Value
        EmanBaja += 1


def Pop():
    global Bus
    global EmanBaja

    if EmanBaja == 0:
        print("Ajao bahi Please bus me beth jao")
    else:
        EmanBaja -= 1
        print(EmanBaja)


Push("Anas")
Push("effie")
print(Bus)

Push("effie")
print(Bus)
Pop()
Push("effie22")
print(Bus)
