from typing import Any, Optional


class Node:
    def __init__(self, val: Any, next: Optional["Node"]):
        self.val = val
        self.next = next

def remove_after(node: Optional[Node]):
    if node is None or node.next is None:
        return

    node.next = node.next.next
