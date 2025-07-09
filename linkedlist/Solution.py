class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# 146 LRU Cache
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.latest = Node(0, 0)
        self.oldest = Node(0, 0)
        self.latest.prev = self.oldest
        self.oldest.next = self.latest

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.oldest.next
            self.remove(lru)
            self.cache.pop(lru.key)

    def insert(self, node):
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 92 Reverse Linked List II
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left-1):
            prev = prev.next

        cur = prev.next
        for _ in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
    

    # 61 Rotate List
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        length = 0
        while dummy.next:
            dummy = dummy.next
            length += 1
        
        position = k % length
        if position == 0:
            return head
            
        cur = head

        for _ in range(length - position - 1):
            cur = cur.next
        
        new_head = cur.next
        dummy.next = head
        cur.next = None
        return new_head
    

    # 19 Remove Nth Node From End of List
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy

        for _ in range(n):
            right = right.next

        while right.next:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        return dummy.next