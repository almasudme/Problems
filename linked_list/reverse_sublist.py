"""
Difficulty Level Hard
We are given a linked list and positions m and n. We need to reverse the linked list from position m to n.
"""

# useful explanations: https://stackoverflow.com/questions/22507197/merging-two-sorted-linked-lists-into-one-linked-list-in-python/40794749

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

def reverse_sublist(L:Node, start: int, finish: int) ->Node:
    dummy=sublist_head=Node(0,L)
    for _ in range(1,start):
        sublist_head = sublist_head.next

    #now reverse
    sublist_iter=sublist_head.next
    for _ in range (finish - start):
        temp=sublist_iter.next
        sublist_iter.next,temp.next,sublist_head.next = temp.next,sublist_head.next,temp
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

m1=Node("1")
m2=Node("1")
m3=Node("2")
m4=Node("4")
m5=Node("11")
m6=Node("3")
m7=Node("5")
m8=Node("7")
m9=Node("2")
L1.head=m1
m1.next=m2
m2.next=m3
m3.next=m4
m4.next=m5
m5.next=m6
m6.next=m7
m7.next=m8
m8.next=m9

L1.listprint()
n=reverse_sublist(L1.head,4,8)
L=LinkedList()
L.head=n
L.listprint()




    