import sys


pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def is_balanced(line: str) -> bool:
    stack = []

    for char in line:
        if char in pairs:
            stack.append(char)
            continue

        # `line` is a closing paren. Check that the last pushed paren matches.
        if len(stack) == 0:
            return False

        last = stack.pop()
        if char != pairs[last]:
            return False

    return len(stack) == 0


for line in sys.stdin:
    line = line.rstrip("\n")
    print(is_balanced(line))
