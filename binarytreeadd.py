class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data)

        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        
        if self.right:
            self.right.postorder()
        
        print(self.data)

    def preorder(self):
        print(self.data)
        
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()



# METHOD 2
# def insert(root: Node | None, value):
#     if root is None:
#         return Node(value)

#     if value < root.data:
#         root.left = insert(root.left, value) 
    
#     elif value > root.data:
#         root.right = insert(root.right, value) 
    
#     return root



root = Node(10)

root.insert(5)
root.insert(20)
root.insert(3)
root.insert(7)

root.inorder()    # 3 5 7 10 20
root.preorder()   # 10 5 3 7 20
root.postorder()  # 3 7 5 20 10