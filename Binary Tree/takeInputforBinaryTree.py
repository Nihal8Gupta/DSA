# Taking input for Binary Tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printTree(root):
    if root is None:
        return
    print(root.data,end=':')
    if root.left is not None:
        print('L',root.left.data,end=',')
    if root.right is not None:
        print('R',root.right.data,end='')
    print()
    printTree(root.left)
    printTree(root.right)

def takeInput():
    rootvalue = int(input())
    if rootvalue == -1:
        return
    root = BinaryTreeNode(rootvalue)
    left = takeInput()
    right = takeInput()
    root.left =left
    root.right =right
    return root

root = takeInput()
printTree(root)