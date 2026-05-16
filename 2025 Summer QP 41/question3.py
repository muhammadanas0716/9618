class Node:
    def __init__(self, NodeDataP):
        self.__NodeData = NodeDataP
        self.__LeftNode = -1
        self.__RightNode = -1
    
    def GetLeft(self):
        return self.__LeftNode

    def GetRight(self):
        return self.__RightNode
    
    def SetLeft(self, value):
        self.__LeftNode = value
    
    def SetRight(self, value):
        self.__RightNode = value

    def GetData(self):
        return self.__NodeData


node1 = Node(10)
node2 = Node(20)
node3 = Node(5)
node4 = Node(15)
node5 = Node(7)

class Tree:
    def __init__(self, FirstNodeP):
        self.__FirstNode = FirstNodeP
    
    def GetRootNode(self):
        return self.__FirstNode

    def Insert(self, node):
        if node < self.__FirstNode:
            pass


# 18 / 30

