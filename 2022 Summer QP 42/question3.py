class Card:
    def __init__(self, NumberP, ColourP):
        self.__Number = NumberP
        self.__Colour = ColourP

    def getNumber(self):
        return self.__Number

    def getColour(self):
        return self.__Colour
    



CardArray = [Card(0, "") for i in range(30)]
try:
    file = open("CardValues.txt", "r")

    for i in range(30):
        number = int(file.readline().strip())
        colour = file.readline().strip()

        CardArray[i] = Card(number, colour)

    file.close()

except FileNotFoundError:
    print("File was not found.")


takenCards = []
def ChooseCard():
    global takenCards

    while True:
        value = int(input("Enter a card number: "))
        if value >= 1 or value <= 30:
            if value not in takenCards:
                takenCards.append(value)
                return value - 1
            else:
                print(f"Already taken man")
        else:
            print("Value between 1 and 30")


Player1 = [Card(0, "") for i in range(4)]

choice1 = ChooseCard()
Player1[0] = CardArray[choice1]

choice2 = ChooseCard()
Player1[1] = CardArray[choice2]

choice3 = ChooseCard()
Player1[2] = CardArray[choice3]

choice4 = ChooseCard()
Player1[3] = CardArray[choice4]

for card in Player1:
    print(f"CardNumber: {card.getNumber()} | CardColour: {card.getColour()}")


# 27 / 27