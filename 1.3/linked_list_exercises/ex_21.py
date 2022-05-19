from typing import Optional


class Node:
    def __init__(self, val: str, next: Optional["Node"]):
        self.val = val
        self.next = next

def build_ll(strs: list[str]) -> Optional[Node]:
    cur = None
    for s in strs:
        cur = Node(s, cur)
    return cur

def print_ll(head: Optional[Node]):
    while head:
        print(f"{head.val} ", end="")
        head = head.next
    print("")

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
