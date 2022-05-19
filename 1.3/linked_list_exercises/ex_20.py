from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional["Node"]):
        self.val = val
        self.next = next

def delete(k: int, head: Node) -> Optional[Node]:
    """Returns the new head node. Assumes valid input."""
    if k == 0:
        return head.next

    cur = head
    while k > 0 and cur is not None:
        k -= 1
        prev = cur
        cur = cur.next

    if cur is not None:
        prev.next = cur.next

    return head

def build_ll(n: int) -> Node:
    cur = None
    for i in range(n):
        cur = Node(i, cur)
    return cur

def print_ll(head: Node):
    while head:
        print(f"{head.val} ", end="")
        head = head.next
    print("")

print("+++delete first item")
case = build_ll(5)
print("before: ", end="")
print_ll(case)
case = delete(0, case)
print("after: ", end="")
print_ll(case)

print("+++delete where k > len(ll)")
print("before: ", end="")
print_ll(case)
case = delete(400, case)
print("after: ", end="")
print_ll(case)

print("+++delete from the middle")
print("before: ", end="")
print_ll(case)
case = delete(2, case)
print("after: ", end="")
print_ll(case)

print("+++delete one item from one-item ll")
case = build_ll(1)
print("before: ", end="")
print_ll(case)
case = delete(0, case)
print("after: ", end="")
print_ll(case)
