def peek(stack: list[int]) -> int:
    if len(stack) == 0:
        raise IndexError("Empty stack.")

    return stack[-1]


cases = [
    [1, 2, 3],
    [1],
    [],
]

for case in cases:
    print(peek(case))
