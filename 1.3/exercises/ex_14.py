from typing import Optional


class FixedArrayQueueOfInts:
    """As always, assuming valid function input."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = 0
        self.head = 0
        self.tail = 0
        self.queue: list[Optional[int]] = [None for _ in range(capacity)]

    def enqueue(self, elem: int):
        if self.items == self.capacity:
            raise IndexError("full queue")

        self.queue[self.tail] = elem
        self.items += 1
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self) -> int:
        if self.items == 0:
            raise IndexError("empty queue")

        elem = self.queue[self.head]
        self.items -= 1
        self.head = (self.head + 1) % self.capacity
        return elem


class ResizingArrayQueueOfInts:
    """As always, assuming valid function input."""

    def __init__(self):
        self.items = 0
        self.head = 0
        self.tail = 0
        self.queue: list[Optional[int]] = [None]

    def resize(self, size):
        temp_q: list[Optional[int]] = [None for _ in range(size)]

        for i in range(self.items):
            temp_q[i] = self.queue[self.head]
            self.head = (self.head + 1) % len(self.queue)

        self.queue = temp_q
        self.head = 0
        self.tail = self.items

    def enqueue(self, elem: int):
        if self.items == len(self.queue):
            self.resize(2 * self.items)

        self.queue[self.tail] = elem
        self.items += 1
        self.tail = (self.tail + 1) % len(self.queue)

    def dequeue(self) -> int:
        if self.items == 0:
            raise IndexError("empty queue")

        if self.items <= len(self.queue) / 4:
            self.resize(len(self.queue) // 2)

        elem = self.queue[self.head]
        self.queue[self.head] = None
        self.items -= 1
        self.head = (self.head + 1) % len(self.queue)
        return elem


# Fixed Queue
test_queue = FixedArrayQueueOfStrings(3)
[test_queue.enqueue(i) for i in range(1, 4)]
[print(test_queue.dequeue()) for _ in range(3)]

try:
    test_queue.dequeue()
except:
    print("all good")

[test_queue.enqueue(i) for i in range(1, 4)]
try:
    test_queue.enqueue(4)
except:
    print("all good")

print(test_queue.dequeue())
test_queue.enqueue(4)
[print(test_queue.dequeue()) for _ in range(3)]


# Resizing Queue
test_queue = ResizingArrayQueueOfStrings()
[test_queue.enqueue(i) for i in range(1, 5)]
[print(test_queue.dequeue()) for _ in range(4)]

try:
    test_queue.dequeue()
except:
    print("all good")

[test_queue.enqueue(i) for i in range(1, 15)]
[print(test_queue.dequeue()) for _ in range(4)]
[test_queue.enqueue(i) for i in range(15, 18)]
print(test_queue.queue)
