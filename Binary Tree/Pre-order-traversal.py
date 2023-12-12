# Pre Order traversal
class Nodetree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preprint(root):
    if root is None:
        return
    
    print(root.data)
    preprint(root.left)
    preprint(root.right)



def takeInput():
    value = int(input())
    if value == -1:
        return
    root = Nodetree(value)
    left = takeInput()
    right = takeInput()
    root.left = left
    root.right = right
    return root

root = takeInput()
preprint(root)