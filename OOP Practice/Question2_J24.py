class Tree:
    def __init__(self, TreeNameP, HeightGrowthP, MaxHeightP, MaxWidthP, EvergreenP):
        self.__TreeName = TreeNameP
        self.__HeightGrowth = HeightGrowthP
        self.__MaxHeight = MaxHeightP
        self.__MaxWidth = MaxWidthP
        self.__Evergreen = EvergreenP


    def GetTreeName(self):
        return self.__TreeName
    
    def GetGrowth(self):
        return self.__HeightGrowth
    
    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetHeightWidth(self):
        return self.__MaxHeight 

    def GetEvergreen(self):
        return self.__Evergreen
    

def ReadData(file="Trees.txt"):
    Trees = [] # ARRAY OF Tree

    try:
        treesData = open(file, "r")
        for tree in treesData:
            TreeName = tree.strip().split(",")[0]
            HeightGrowth = tree.strip().split(",")[1]
            MaxHeight = tree.strip().split(",")[2]
            MaxWidth = tree.strip().split(",")[3]
            Evergreen = tree.strip().split(",")[4]

            treeInstance = Tree(TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen)
            Trees.append(treeInstance)
        treesData.close()
    except FileNotFoundError:
        print("File was not found.")
    
    return Trees

def PrintTrees(Tree):
    if Tree.GetEvergreen() == "Yes":
        print(f"{Tree.GetTreeName()} has a maximum height {Tree.GetMaxHeight()} a maximum width {Tree.GetMaxWidth()} and grows {Tree.GetGrowth()} cm a year. It does not lose its leaves.")
    else:
        print(f"{Tree.GetTreeName()} has a maximum height {Tree.GetMaxHeight()} a maximum width {Tree.GetMaxWidth()} and grows {Tree.GetGrowth()} cm a year. It loses its leaves each year")


treesArray = ReadData("Trees.txt")

PrintTrees(treesArray[0])
