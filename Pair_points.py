class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self, head=None):
        self.head = head

def cycle(list):
    slow = list.head
    fast = list.head
    point = False
    while fast is not None and fast.nxt is not None:
        slow = slow.nxt
        fast = fast.nxt.nxt
        if slow == fast:
            met = True
            break
    if not met:
            return None
    else:
        slow = list.head
        while  slow != fast:
               slow = slow.nxt
               fast = fast.nxt
        return slow

def find_double(bloc):
    slow = 0
    fast = 0
    while True:
        slow = bloc[slow]
        fast = bloc[bloc[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast :
        slow = bloc[slow]
        fast = bloc[fast]
    return slow
















