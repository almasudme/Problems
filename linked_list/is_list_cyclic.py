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
#L.listprint() # will print infinitely



