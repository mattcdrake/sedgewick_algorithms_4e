from typing import Optional

from node import Node, build_ll, print_ll


def find(key: str, head: Optional[Node]) -> bool:
    while head is not None:
        if head.val == key:
            return True
        head = head.next
    return False

cases_input = [
    ["wow", "nice", "needle", "i", "guess"],
    ["this", "haystack", "is", "empty"],
    ["needle"],
    [],
]

cases = [build_ll(case) for case in cases_input]
for i, case in enumerate(cases):
    print(f"test {i}:")
    print_ll(case)
    print(f"found 'needle'? {find('needle', case)}\n")
