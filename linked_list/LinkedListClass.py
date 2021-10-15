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