"""
...create ll...

cur = ll.first
if cur.next is None:
    ll.first = None
    return

while cur.next is not None:
    prev = cur
    cur = cur.next

prev.next = None
"""
