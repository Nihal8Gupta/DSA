# Queue (LIFO) or Stack

from queue import LifoQueue
q = LifoQueue()
#Insertion of Lifoqueue
q.put(11)
q.put(12)
q.put(13)
#it will return True if Lifoqueue is empty
q.empty()
# size of Lifoqueue
q.qsize()
# poping the element

while not q.empty():
    print(q.get())