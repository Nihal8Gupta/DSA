#6- Insert the element at the nth index position
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def takeInput():
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

def insert(head,reqposition):
    index=0
    while head != None:
        if reqposition == index:
            newval = int(input("new value="))
            node = Node(newval)
            node.next = head.next
            head.next = node
            break
        index += 1
        head = head.next

head = takeInput()
reqposition = int(input())
insert(head,reqposition-1)
display(head) 