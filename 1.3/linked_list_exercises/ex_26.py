from typing import Optional

from node import Node, build_ll, print_ll


def remove(key: str, head: Optional[Node]) -> Optional[Node]:
    """Returns new head."""
    if head is None:
        return

    while head.val == key:
        if head.next is None:
            return
        head = head.next

    orig, prev, head = head, head, head.next
    while head is not None:
        if head.val == key:
            prev.next = head.next
        prev, head = head, head.next

    return orig


cases = [
    ["haystack", "haystack", "needle", "haystack"],
    ["haystack", "haystack", "needle"],
    ["needle"],
    ["haystack"],
]


for case in cases:
    test = build_ll(case)
    print("before: ", end="")
    print_ll(test)
    after = remove("needle", test)
    print("after: ", end="")
    print_ll(after)
