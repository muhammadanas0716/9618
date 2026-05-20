class Node:
    def __init__(self, DataP):
        self.__LeftPointer = -1
        self.__Data = DataP
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer
    
    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data
    
    def SetLeft(self, value):
        self.__LeftPointer = value
    
    def SetRight(self, value):
        self.__RightPointer = value

    def SetData(self, value):
        self.__Data = value

class TreeClass:
    def __init__(self):
        self.__FirstNode = -1
        self.__NumberNodes = 0
        self.__Tree = [Node(-1) for i in range(20)]

    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__FirstNode = 0
            self.__NumberNodes += 1

        else:
            self.__Tree[self.__NumberNodes] = NewNode
            CurrentNode = self.__FirstNode

            while CurrentNode != -1:
                PreviousNode = CurrentNode

                if NewNode.GetData() < self.__Tree[CurrentNode].GetData():
                    CurrentNode = self.__Tree[CurrentNode].GetLeft()
                    Direction = "left"
                else:
                    CurrentNode = self.__Tree[CurrentNode].GetRight()
                    Direction = "right"

            if Direction == "left":
                self.__Tree[PreviousNode].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[PreviousNode].SetRight(self.__NumberNodes)

            self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for i in range(self.__NumberNodes):
                print(
                    self.__Tree[i].GetLeft(),
                    self.__Tree[i].GetData(),
                    self.__Tree[i].GetRight()
                )


# 26 / 30