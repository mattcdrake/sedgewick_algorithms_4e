def include_parens(expr: str) -> str:
    """Assuming string input is valid."""
    operands = []
    operators = []

    pieces = expr.split(" ")
    for piece in pieces:
        if piece == ")":
            right = operands.pop()
            left = operands.pop()
            op = operators.pop()
            operands.append(f"( {left} {op} {right} )")
            continue

        if piece.isnumeric():
            operands.append(piece)
        else:
            operators.append(piece)

    return operands[0]


cases = [
    "1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )",
]
for case in cases:
    print(include_parens(case))
