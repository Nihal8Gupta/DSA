#Queue (FIFO)
from queue import Queue
q = Queue()
#Insertion of queue
q.put(11)
q.put(12)
q.put(13)
#it will return True if queue is empty
q.empty()
# size of queue
q.qsize()
# poping the element
q.get()         # return  11
while not q.empty():
    print(q.get())