class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
         
if __name__ == '__main__':
    head = Node(100)
    head.next = Node(50)
    head.next.next = Node(10)
    print(head.data)
    print(head.next.data)
    print(head.next.next.data)


    