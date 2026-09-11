class Node:
    def __init__(self,val=0,key=0):
        self.val = val
        self.key = key
        self.next = self.prev = 0
       

class LRUCache:

    def __init__(self, capacity: int):
         self.capacity = capacity 
         self.cache = {}
         self.right, self.left = Node(),Node()
         self.left.next,self.right.prev = self.right,self.left

    def insert(self,node):
        node.next,node.prev = self.right,self.right.prev
        self.right.prev.next = node 
        self.right.prev = node

        

    def remove(self,node):
        node.prev.next,node.next.prev = node.next,node.prev
        
           
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
           
        self.cache[key] = Node(value,key)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
          lru = self.left.next 
          self.remove(lru)
          del self.cache[lru.key]

      

        

        
