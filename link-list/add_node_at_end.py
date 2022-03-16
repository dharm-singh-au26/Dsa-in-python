class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = None

def AddNodeAtEnd(x):
    global head
    
    if head == None:
        head = Node(x) 
        return
    cur = head
    while cur.next != None :
        cur = cur.next
    cur.next = Node(x)

def printlinklist():
    global head

    cur = head

    while cur != None :
        print(cur.data)
        cur = cur.next

if __name__ == '__main__':
    AddNodeAtEnd(10)
    AddNodeAtEnd(20)
    AddNodeAtEnd(30)
    AddNodeAtEnd(40)

    # print("head element",head.data)
    # print("2nd element",head.next.data)
    # print("3re element",head.next.next.data)
    # print("4th element",head.next.next.next.data)

    printlinklist() 


