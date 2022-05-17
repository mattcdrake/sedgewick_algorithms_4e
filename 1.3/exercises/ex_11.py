def infix_to_postfix(expr: str) -> str:
    """Assuming string input is valid."""
    operands = []
    operators = []

    pieces = expr.split(" ")
    for piece in pieces:
        if piece == "(":
            continue

        if piece == ")":
            right = operands.pop()
            left = operands.pop()
            op = operators.pop()
            operands.append(f"{left} {right} {op}")
            continue

        if piece.isnumeric():
            operands.append(piece)
        else:
            operators.append(piece)

    return operands[0]


def apply_op(op: str, l: int, r: int) -> int:
    """Only supports the most basic of arithmetic"""
    if op == "+":
        return l + r
    if op == "-":
        return l - r
    if op == "*":
        return l * r
    return l // r


def evaluate_postfix(expr: str) -> int:
    """Assuming string input is valid."""
    operands = []

    pieces = expr.split(" ")
    for piece in pieces:
        try:
            num = int(piece)
            operands.append(num)
        except:
            right = operands.pop()
            left = operands.pop()
            operands.append(apply_op(piece, left, right))

    return operands[0]


cases = ["( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )"]

for case in cases:
    print(evaluate_postfix(infix_to_postfix(case)))
