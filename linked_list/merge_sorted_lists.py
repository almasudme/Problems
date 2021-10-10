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

L1.listprint()
L2.listprint()
    