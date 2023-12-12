# Sum of Nodes of BinaryTree
class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
def takeInput():
    value = int(input())
    if value == -1:
        return
    root = BinaryTreeNode(value)
    left = takeInput()
    right = takeInput()
    root.left = left
    root.right = right
    return root
def printTree(root):
    if root is None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print("L",root.left.data,end=",")
    if root.right is not None:
        print("R",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)
def sumNode(root):
    if root is None:
        return 0
    
    return root.data + sumNode(root.left) + sumNode(root.right)

root = takeInput()
printTree(root)
print('Sum of Node data:',sumNode(root))