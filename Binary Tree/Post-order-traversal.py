#Post order
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postprint(root):
    if root is None:
        return 
    
    postprint(root.left)
    postprint(root.right)
    print(root.data)

def takeInput():
    value = int(input())
    if value == -1:
        return
    root = TreeNode(value)
    left = takeInput()
    right = takeInput()
    root.left = left
    root.right = right
    return root
root = takeInput()
postprint(root)