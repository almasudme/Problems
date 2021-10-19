class Node:
    def __init__(self,data = None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self,root=Node):
        self.root=root
    
    def preorder_traverse(self,root:Node)->None:
        if root:
            print(f"Preorder: {root.data}")
            self.preorder_traverse(root.left)
            self.preorder_traverse(root.right)

    def inorder_traverse(self,root:Node)->None:
        if root:
            
            self.inorder_traverse(root.left)
            print(f"inorder: {root.data}")
            self.inorder_traverse(root.right)

    def postorder_traverse(self,root:Node)->None:
        if root:
            
            self.postorder_traverse(root.left)
            self.postorder_traverse(root.right)
            print(f"postorder: {root.data}")
    





# create Tree
root=Node(1)

tree=BinaryTree(root)

tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.postorder_traverse(root)
