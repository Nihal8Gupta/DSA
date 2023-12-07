# 1 Creation of Node of Binary Tree
#A binary tree is a tree data structure in which each parent node can have at most two children. Each node of a binary tree consists of three items:
class BinaryTreeNode:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None
bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(3)
bt3 = BinaryTreeNode(5)
print(bt1,'Data:',bt1.data,'left:',bt1.left,'right:',bt1.right) 
print(bt2,'Data:',bt2.data,'left:',bt2.left,'right:',bt2.right)
print(bt3,'Data:',bt3.data,'left:',bt3.left,'right:',bt3.right)

# making connection b/w Nodes
bt1.left = bt2
bt1.right = bt3
print('After connection:')
print(bt1,'Data:',bt1.data,'left:',bt1.left,'right:',bt1.right) 
print(bt2,'Data:',bt2.data,'left:',bt2.left,'right:',bt2.right)
print(bt3,'Data:',bt3.data,'left:',bt3.left,'right:',bt3.right)