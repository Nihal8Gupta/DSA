#4- Print elements of linked list
class Node:  #Creation of node
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():    #Taking elements and making connection between nodes
    ele = [int(i) for i in input().split()]
    head = None
    tail = None
    for curval in ele:
        if curval == -1:
            break
        else:
            node = Node(curval)
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
    return head
def display(head):  #Printing elements of linkedlist
    while head != None:
        print(head.data)
        head = head.next

head = takeInput()
display(head)