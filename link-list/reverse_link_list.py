# Reverse link list :-

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printlinklist(head):
    cur = head
    while cur != None:
        print(cur.data,end=" ")
        cur = cur.next

def reverse_link_list(head):
    prev = None
    cur = head
    while cur != None :
        nxt = cur.next
        cur.next = prev 
        prev = cur
        cur = nxt
    return prev


if __name__ == '__main__':
    head = Node(5)
    head.next = Node(4)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    printlinklist(head)
    print()

    printlinklist(reverse_link_list(head))
    
    