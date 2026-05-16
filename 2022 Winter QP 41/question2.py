class Card:
    def __init__(self, NumberP, ColourP):
        self.__Number = NumberP
        self.__Colour = ColourP

    def getNumber(self):
        return self.__Number
    
    def getColour(self):
        return self.__Colour
    
OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")

OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")

OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [Card(0, "") for i in range(10)]
        self.__FirstCard = 0
        self.__NumberCards = 5

        self.__Cards[0] = Card1
        self.__Cards[1] = Card2
        self.__Cards[2] = Card3
        self.__Cards[3] = Card4
        self.__Cards[4] = Card5

    def GetCard(self, index):
        return self.__Cards[index]
    


player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow)
player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)


def CalculateValue(playerHand: Hand):
    score = 0
    for i in range(5):
        card = playerHand.GetCard(i)
        if card.getColour() == "red":
            score += 5
        elif card.getColour() == "blue":
            score += 10
        else:
            score += 15
    
    return score


player1Score = CalculateValue(player1)
player2Score = CalculateValue(player2)

if player1Score > player2Score:
    print(f"Player 1 has {player1Score} and Player 2 has {player2Score} hence player1 has one")
elif player1Score < player2Score:
    print(f"Player 1 has {player1Score} and Player 2 has {player2Score} hence player2 has one")
else:
    print(f"Player 1 has {player1Score} and Player 2 has {player2Score} hence a draw")




# 30 / 31