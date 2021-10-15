# useful explanations: https://stackoverflow.com/questions/22507197/merging-two-sorted-linked-lists-into-one-linked-list-in-python/40794749
from LinkedListClass import Node,LinkedList



def merge_two_sorted_lists(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    dummy=tail=Node()
    while (head1 and head2):
        if head1.data < head2.data:
            
            tail.next, head1 = head1,head1.next
        else:
            
            tail.next,head2 = head2,head2.next

        tail=tail.next
        print(tail.data)
    tail.next = head1 
    return dummy.next



L1=LinkedList()
L2=LinkedList()
m1=Node("1")
m2=Node("1")
m3=Node("2")
m4=Node("4")
m1.next=m2
m2.next=m3
m3.next=m4
L1.head=m1

n1=Node("1")
n2=Node("3")
n1.next=n2
L2.head=n1

# L1.listprint()
# L2.listprint()

n = merge_two_sorted_lists(m1,n1)
L=LinkedList()
L.head=n
L.listprint()

    