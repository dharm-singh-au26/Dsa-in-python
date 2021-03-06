# # merge two sorted link list :-

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

# head = None
def printlist(head):
    # global head

    cur = head
    while cur != None :
        print(cur.data,end =" ")
        cur = cur.next

def merge(head1,head2):
    p1 = head1
    p2 = head2 
    
    head3 = None
    cur = head3

    while p1 != None and p2 != None :
        if p1.data < p2.data :
            if head3 is None :
                head3 = Node(p1.data)
                cur = head3
            else:
                cur.next = Node(p1.data)
                cur = cur.next
            p1 = p1.next
        else:
            if head3 is None:
                head3 = Node(p2.data)
                cur = head3
            else:
                cur.next =Node(p2.data)
                cur = cur.next
            p2 = p2.next
        
        while p1 != None:
            cur.next = Node(p1.data)
            cur = cur.next
            p1 = p1.next
        
        while p2 != None:
            cur.next = Node(p2.data)
            cur = cur.next
            p2 = p2.next
        
        return head3
    
if __name__=="__main__":
    
    head1 = Node(5)
    head1.next = Node(15)
    head1.next.next = Node(25)
    head1.next.next.next = Node(125)

    printlist(head1)
    print()

    head2 = Node(1)
    head2.next = Node(3)
    head2.next.next = Node(6)
    head2.next.next.next = Node(15)
    head2.next.next.next.next = Node(19)
    printlist(head2)
    print()

    head3 = merge(head1,head2)
    printlist(head3)
