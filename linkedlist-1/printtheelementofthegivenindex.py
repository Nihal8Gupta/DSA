#5- Print element of nth index position of the linkedlist
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

def display(head,reqposition):
    index=0
    while head is not None:
        if reqposition == index:
            print(head.data)
            break
        index += 1
        head = head.next
    else:
        print('Index out of range')
head = takeInput()
reqposition =int(input())
display(head,reqposition)