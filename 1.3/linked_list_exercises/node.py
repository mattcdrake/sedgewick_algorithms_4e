from typing import Any, Optional


class Node:
    def __init__(self, val: Any, next: Optional["Node"] = None):
        self.val = val
        self.next = next


def print_ll(head: Optional[Node]):
    while head:
        print(f"{head.val} ", end="")
        head = head.next
    print("")


def build_ll(items: list[Any]) -> Optional[Node]:
    cur = None
    for item in items:
        cur = Node(item, cur)
    return cur
