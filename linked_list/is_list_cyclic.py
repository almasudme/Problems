from LinkedListClass import Node,LinkedList


f=Node(7)
e=Node(9,f)
d=Node(2,e)
c=Node(4,d)
b=Node(3,c)
a=Node(1,b)
"""
1-3-4-2
      |
    7-9
"""
f.next=c # This introduces a cycle 
"""
1-3-4-2
    |  |
    7-9
"""

L=LinkedList()
L.head=a
# L.listprint() # will print infinitely

def is_cyclic(head):

    def cycle_len(end):
        start = end
        step=0
        while True:
            step=step+1
            start=start.next
            
            if start is end:
                return step
            


    slow=fast=head
    while  fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow is  fast: 
            advanced_i =head

            for _ in range(cycle_len(slow)):
                advanced_i =advanced_i.next
            it = head
            while it is not advanced_i:
                it=it.next
                advanced_i=advanced_i.next
            return it
    return False
print(is_cyclic(a).data)





