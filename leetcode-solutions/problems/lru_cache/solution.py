class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.map:
            # Since the key is accessed
            # Update the location - remove the current one
            # add to the right
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key already exists, remove the exisiting one
        # coz the value is being updated - remove the reference
        # from the map
        if key in self.map:
            self.remove(self.map[key])
        # Now create a new node and add to the map
        self.map[key] = Node(key, value)
        self.insert(self.map[key])

        # If the capacity is exceeded, then remove the LRU
        if len(self.map) > self.capacity:
            n = self.left.next
            self.remove(n)
            del self.map[n.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)