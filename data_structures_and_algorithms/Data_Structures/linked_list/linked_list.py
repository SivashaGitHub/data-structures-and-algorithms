class LinkedList:
  
    def __init__(self):
        self.head = None

    def insert(self,value):
        self.head = Node(value,self.head)

    def includes(self,key):
        current = self.head

        while current:
            if current.value == key:
                return True
            
            current = current.next
        
        return False
    # "{ a } -> { b } -> { c } -> NULL"
    
    #def __str__ (self):
    def toString(self):     
        str =""
        current = self.head
        
        while current:
            str += "{ " + current.value + " } -> "                
            current = current.next
        str += "NULL"
        #print (str)    
        return str
            
class Node:
    def __init__(self,value,next = None):
        self.value =value
        self.next = next
        


