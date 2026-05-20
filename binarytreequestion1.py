# DECLARE ArrayNodes: [0:19, 0:2] OF INTEGER
global ArrayNodes
ArrayNodes = [[-1, -1, -1] for i in range(20)]

FreeNode = 6
RootPointer = 0

ArrayNodes[0][0], ArrayNodes[0][1], ArrayNodes[0][2] = 1, 20, 5
ArrayNodes[1][0], ArrayNodes[1][1], ArrayNodes[1][2] = 2, 15, -1
ArrayNodes[2][0], ArrayNodes[2][1], ArrayNodes[2][2] = -1, 3, 3
ArrayNodes[3][0], ArrayNodes[3][1], ArrayNodes[3][2] = -1, 9, 4
ArrayNodes[4][0], ArrayNodes[4][1], ArrayNodes[4][2] = -1, 10, -1
ArrayNodes[5][0], ArrayNodes[5][1], ArrayNodes[5][2] = -1, 58, -1
ArrayNodes[6][0], ArrayNodes[6][1], ArrayNodes[6][2] = -1, -1, -1

def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root # CHECK
        else:
            if ArrayNodes[Root][1] == -1:
                return -1

    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    

def PostOrder(rootNode):
    # left, right, root
    if rootNode[0] != -1:
        return PostOrder(rootNode[0])

    if rootNode[2] != -1:
        return PostOrder(rootNode[2])

    print(str(rootNode[1]))




