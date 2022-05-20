from typing import Any

from node import Node


class Queue:
    def __init__(self):
        self.last = None

    def enqueue(self, val: Any):
        new_node = Node(val)

        if self.last is None:
            new_node.next = new_node
            self.last = new_node
            return

        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    def dequeue(self) -> Node:
        if self.last is None:
            raise IndexError("empty queue")

        if self.last.next == self.last:
            elem = self.last
            self.last = None
        else:
            elem = self.last.next
            self.last.next = elem.next

        return elem

    def print(self):
        if self.last is None:
            print("empty queue")
            return

        cur = self.last
        while True:
            print(cur.val)
            cur = cur.next
            if cur == self.last:
                return


q = Queue()
q.enqueue(1)
q.print()
print(f"got: {q.dequeue().val}")
q.print()

[q.enqueue(i) for i in range(5)]
for i in range(5):
    print(f"got: {q.dequeue().val}")
    q.print()
