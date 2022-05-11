class FullStackError(Exception):
    pass


class EmptyStackError(Exception):
    pass


class FixedCapacityStackOfStrings:
    """Port of the book's Java class for this exercise."""

    def __init__(self, cap: int):
        self.cap = cap
        self.stack = []

    def push(self, item: str):
        if len(self.stack) >= self.cap:
            raise FullStackError("Full stack.")

        self.stack.append(item)

    def pop(self) -> str:
        if len(self.stack) == 0:
            raise EmptyStackError("Empty stack.")

        return self.stack.pop()

    def is_empty(self) -> bool:
        return self.size() == 0

    def is_full(self) -> bool:
        return self.size() == self.cap

    def size(self) -> int:
        return len(self.stack)
