class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = None

def dlt_tail_node():
    global head
    prev = Node
    cur = head
    while cur.next != None:
        prev = cur
        cur = cur.next
    prev.next = None

def print_link_list():
    global head
    cur = head
    while cur != None :
        print(cur.data)
        cur = cur.next
        
if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    print_link_list()
    print()
    dlt_tail_node()
    print_link_list()
    print()
    dlt_tail_node()
    print_link_list()
     