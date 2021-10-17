class BTNode:
    def __init__(self,data = None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    
    def tree_traversal(root: BTNode)->None:
        print("Preorder: %d" %root.data)
        tree_traversal(root.left)
        print("Inorder: %d" %root.data)
        tree_traversal(root.right)


# create Tree

a=BTNode("A")

c=BTNode("C")
b=BTNode("B",a,c)
e=BTNode("E")
d=BTNode("D",b,e)

b.tree_traversal()