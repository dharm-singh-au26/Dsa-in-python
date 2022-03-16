class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = None

def AddNodeAtHead(x):
    global head

    if head is None:
        head = Node(x)
        return
    new_node = Node(x)
    new_node.next = head
    head = new_node

def printlinklist():
    global head

    cur = head 
    while cur != None :
        print(cur.data)
        cur = cur.next
    

if __name__ == '__main__':
    AddNodeAtHead(10)
    AddNodeAtHead(20)
    AddNodeAtHead(30)
    AddNodeAtHead(40)
    printlinklist()
    
    