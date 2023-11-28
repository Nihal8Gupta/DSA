#9- Mid poin of the linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeInput():
    head,tail=None,None
    ele = [int(ele) for ele in input().split()]
    for data in ele:
        if data == -1:
            return head
        newNode = Node(data)
        if head is None:
            head,tail = newNode,newNode
        else:
            tail.next = newNode
            tail = newNode
    
    return head

def display(head):
    while head != None:
        print(head.data,end='->')
        head = head.next
    else:
        print(None)

def midpoint(head):
    smallhead =head
    count = 0
    while smallhead != None:
        count += 1
        smallhead = smallhead.next
    mid,target = count//2,1 
    while head != None:
        if target == mid:
            return (head.data+head.next.data)/2 if count%2==0 else head.next.data
        target += 1
        head = head.next

head = takeInput()
display(head)
mid = midpoint(head)

print('Midvalue:',mid)