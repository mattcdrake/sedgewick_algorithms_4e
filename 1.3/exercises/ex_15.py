#!/usr/bin/env python3
import sys
from typing import Any

class ResizingArrayQueue:
    """As always, assuming valid function input."""

    def __init__(self):
        self.items = 0
        self.head = 0
        self.tail = 0
        self.queue: list[Any] = [None]

    def resize(self, size):
        temp_q: list[Any] = [None for _ in range(size)]

        for i in range(self.items):
            temp_q[i] = self.queue[self.head]
            self.head = (self.head + 1) % len(self.queue)

        self.queue = temp_q
        self.head = 0
        self.tail = self.items

    def enqueue(self, elem: Any):
        if self.items == len(self.queue):
            self.resize(2 * self.items)

        self.queue[self.tail] = elem
        self.items += 1
        self.tail = (self.tail + 1) % len(self.queue)

    def dequeue(self) -> Any:
        if self.items == 0:
            raise IndexError("empty queue")

        if self.items <= len(self.queue) / 4:
            self.resize(len(self.queue) // 2)

        elem = self.queue[self.head]
        self.queue[self.head] = None
        self.items -= 1
        self.head = (self.head + 1) % len(self.queue)
        return elem


# Assume len(strings) >= k
q = ResizingArrayQueue()
k = int(sys.argv[1])

for line in sys.stdin:
    words = line.split(" ")
    for word in words:
        if q.items == k:
            q.dequeue()
        q.enqueue(word)

print(q.dequeue())
