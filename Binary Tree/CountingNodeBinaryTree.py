# Counting Node in BinaryTree
class BinaryTreeNode:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None
def takeInput():
    data = int(input())
    if data == -1:
        return
    root = BinaryTreeNode(data)
    left = takeInput()
    right = takeInput()
    root.left = left
    root.right = right
    return root
def printTree(root):
    if root is None:
        return
    print(root.data,end=':')
    if root.left is not None:
        print('L',root.left.data,end=',')
    if root.right is not None:
        print("R",root.right.data,end='')
    print()
    printTree(root.left)
    printTree(root.right)
def countNode(root):
    if root is None:
        return 0
    left = countNode(root.left)
    right = countNode(root.right)
    return left + right + 1

root = takeInput()
printTree(root)
print('Node :',countNode(root))