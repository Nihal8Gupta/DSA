#8- Reverse the linked list (My code)
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
def takeInput():
    ele = [1,2,3,4,-1]
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
    return (head,tail)
def display(head):
    while head != None:
        print(head.data,end="->")
        head = head.next
    print(None)

def reversel(head):            #reverse the linked list
    if head.next is None or head is None:
        return head
    else:
        reversel(head.next).next= head
        return head
     

traverse = takeInput()
display(traverse[0])
reversel(traverse[0])
traverse[0].next=None
print()
display(traverse[1])