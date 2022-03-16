class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = None 

def AddNodeAtK(k,x):
    global head 
    if k <= 0:
        return
    ctr = 1
    cur = head
    while ctr != k:
        cur = cur.next
        ctr += 1 
    nxt_node = cur.next
    new_node = Node(x)
    cur.next = new_node
    new_node.next = nxt_node

def printlinklist():
    global head

    cur = head 
    while cur != None :
        print(cur.data)
        cur = cur.next

if __name__ == '__main__':
    head = Node(100)
    head.next = Node(50)
    head.next.next = Node(10)
    AddNodeAtK(2,15)
    printlinklist()

    
