from typing import Optional

from node import Node, build_ll, print_ll


def max_ll(head: Optional[Node]) -> int:
    if head is None:
        return 0

    max_seen = 0
    while head is not None:
        max_seen = max(head.val, max_seen)
        head = head.next

    return max_seen


cases = [
    [1, 2, 3, 4, 5],
    [],
    [42],
    [4, 8, 15, 16, 23, 42],
]
for case in cases:
    ll = build_ll(case)
    print("list:")
    print_ll(ll)
    print(f"max: {max_ll(ll)}")
