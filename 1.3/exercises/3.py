"""
b) 4 6 8 7 5 3 2 9 0 1 is impossible:

push 0-4
stack: 0 1 2 3 4

pop 4
stack: 0 1 2 3

push 5-6
stack: 0 1 2 3 5 6

pop 6
stack: 0 1 2 3 5

push 7-8
stack: 0 1 2 3 5 7 8

pop 8
stack: 0 1 2 3 5 7

pop 7
stack: 0 1 2 3 5

pop 5
stack: 0 1 2 3

pop 3
stack: 0 1 2

pop 2
stack: 0 1

push 9
stack: 0 1 9

pop 9
stack: 0 1

pop 0 (nope! there's a 1 there)
"""
