class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def listprint(self):
      printval = self.head
      while printval is not None:
         print (printval.data, end=" ")
         printval = printval.next
      print("\n")


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


#===========================
# Sample code for node creation
# L1=LinkedList()
# n1=Node("1")
# n2=Node("Tue")
# n1.next=n2
# L1.head=n1
# L1.listprint()
#===========================

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

    