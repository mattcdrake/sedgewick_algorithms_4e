from typing import Any, Optional


class Node:
    def __init__(self, val: Any, next: Optional["Node"]):
        self.val = val
        self.next = next

def print_ll(head: Optional[Node]):
    while head:
        print(f"{head.val} ", end="")
        head = head.next
    print("")

def build_ll(strs: list[str]) -> Optional[Node]:
    cur = None
    for s in strs:
        cur = Node(s, cur)
    return cur

def insert_after(first: Optional[Node], second: Optional[Node]):
    """Assuming that the rest of second's linked-list should be inserted as well."""
    if first is None or second is None:
        return

    after_first = first.next
    second_end = second
    while second_end.next is not None:
        second_end = second_end.next

    first.next = second
    second_end.next = after_first

ll_first = build_ll(["list", "cool", "hey"])
ll_second = build_ll(["alright", "one", "is", "this"])

print_ll(ll_first)
print_ll(ll_second)
print("inserting...")
insert_after(ll_first.next, ll_second)
print_ll(ll_first)
