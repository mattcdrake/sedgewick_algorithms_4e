"""
...create ll...

# Empty list
if ll.first is None:
    return

# One item
if ll.first.next is None:
    ll.first = None
    return

# General case
cur = ll.first
while cur.next is not None:
    prev = cur
    cur = cur.next

prev.next = None
"""
