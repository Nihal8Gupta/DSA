#Taking input with head and without tail
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    head = None
    
    ele=[int(i) for i in input().split()] #[1,2,3,-1]
    for curval in ele:
        if curval == -1:
            break
        else:
            node=Node(curval)
            if head is None:
                head=node 
            else:
                curval = head
                while curval.next is not None:
                    curval=curval.next
                curval.next=node

    return head
head=takeInput()
while head != None:
    print(head.data)
    head=head.next
#it will be increases time complexity so we have to use tail concept here to avoiding inner loop