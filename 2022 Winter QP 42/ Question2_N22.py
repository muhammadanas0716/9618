class Character:
    # DECLARE PRIVATE Name: STRING
    # DECLARE PRIVATE XCoordinate: INTEGER
    # DECLARE PRIVATE YCoordinate: INTEGER

    def __init__(self, NameP, XCoordinateP, YCoordinateP):
        self.__Name = NameP
        self.__XCoordinate = XCoordinateP
        self.__YCoordinate = YCoordinateP

    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
        
    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange


# Create the array
Characters = [Character("", 0, 0) for i in range(10)]


try:
    file = open(file="Characters.txt", mode="r")

    for i in range(10):
        Name = file.readline().strip()
        XPos = int(file.readline().strip())
        YPos = int(file.readline().strip())
        Characters[i]  = Character(Name, XPos, YPos)
    
    file.close()

except FileNotFoundError:
    print("File not found.")


found = False
player_ix = -1
while not found:
    name = input("Enter the name of the character to move: ")
    for i in range(10):
        if Characters[i].GetName().lower() == name.lower():
            name_ix = i
            found = True

while True:
    key = input("Enter your key choice: ")

    if key.upper() == "A":
        Characters[player_ix].ChangePosition(-1, 0)
    elif key.upper() == "W":
        Characters[player_ix].ChangePosition(0, 1)
    elif key.upper() == "S":
        Characters[player_ix].ChangePosition(0, -1)
    elif key.upper() == "D":
        Characters[player_ix].ChangePosition(1, 0)
    elif key.lower() == "exit":
        break
    else:
        print("Enter proper choice please.")

# so idk how this works but i guess you js gootta make it happen liek how does it work idk, but u have to notice