# Max value in BinaryTree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def takeInput():
    rootvalue = int(input())
    if rootvalue == -1:
        return
    root = BinaryTreeNode(rootvalue)
    left = takeInput()
    right = takeInput()
    root.left = left
    root.right = right
    return root
def maxvalue(root):
    if root == None:
        return -1
    left = maxvalue(root.left)
    right = maxvalue(root.right)
    large = max(left,right,root.data)
    return large
root = takeInput()
print('Max :',maxvalue(root))
#1,2,3,4,5,6