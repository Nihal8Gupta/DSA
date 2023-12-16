#Height of Tree
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def takeInput():
    rootvalue = int(input())
    if rootvalue == -1:
        return
    root = TreeNode(rootvalue)
    left = takeInput()
    right = takeInput()
    root.left = left 
    root.right = right
    return root
def printtree(root):
    if root is None:
        return 
    print(root.data,end=":")
    if root.left is not None:
        print('L',root.left.data,end=',')
    if root.right is not None:
        print('R',root.right.data,end='')
    print()
    printtree(root.left) 
    printtree(root.right)

def maxNode(root):
    if root is None:
        return 0
    else:
        LD = maxNode(root.left)
        RD = maxNode(root.right)
        return max(LD,RD)+1
    
root = takeInput()
printtree(root)
print(maxNode(root))