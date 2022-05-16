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


cases = ["( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )"]

for case in cases:
    print(infix_to_postfix(case))
