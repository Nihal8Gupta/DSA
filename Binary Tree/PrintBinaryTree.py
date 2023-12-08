#2 Print Binarytree
class BinaryTreeNode:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None
#print the binarytree
def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(3)
bt3 = BinaryTreeNode(5)
bt1.left = bt2
bt1.right = bt3
printTree(bt1)