#7- Deleting element from the linkedlist
class Node:
    def __init__(self,data) -> None:
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
def display(head):
    while head != None:
        print(head.data)
        head = head.next

def delete(head,reqposition):
    index = 0
    while head != None:
        if reqposition == index:
            temp = head.next
            head.next = temp.next
            break
        head = head.next
        index += 1
head = takeInput()
reqposition = int(input())
delete(head,reqposition-1)
display(head)