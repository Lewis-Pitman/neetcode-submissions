class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.value_dict = {} # Map key -> Node

        # Setup dummy nodes to avoid null checks
        self.dummy_left = Node(0, 0)
        self.dummy_right = Node(0, 0)
        self.dummy_left.next = self.dummy_right
        self.dummy_right.prev = self.dummy_left

    def get(self, key: int) -> int:
        if key in self.value_dict:
            # Must move to "Most Recently Used" (right)
            self._remove_node(self.value_dict[key])
            self._insert_at_right(self.value_dict[key])
            return self.value_dict[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.value_dict:
            self._remove_node(self.value_dict[key])
        
        self.value_dict[key] = Node(key, value)
        self._insert_at_right(self.value_dict[key])

        if len(self.value_dict) > self.capacity:
            # Remove from "Least Recently Used" (left)
            lru = self.dummy_left.next
            self._remove_node(lru)
            del self.value_dict[lru.key]

    def _remove_node(self, node):
        """Standard doubly-linked list removal"""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def _insert_at_right(self, node):
        """Always insert right before the dummy_right"""
        prev, nxt = self.dummy_right.prev, self.dummy_right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt