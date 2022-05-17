"""
"it was - the best - of times - - - it was - the - -"

Start:
a = [null]
n = 0

"it"
a = ["it"]
n = 1

"was"
a = ["it", "was"]
n = 2

"-"
a = ["it", null]
n = 1

"the"
a = ["it", "the"]
n = 2

"best"
a = ["it", "the", "best", null]
n = 3

"-"
a = ["it", "the", null, null]
n = 2

"of"
a = ["it", "the", "of", null]
n = 3

"times"
a = ["it", "the", "of", "times"]
n = 4

"-"
a = ["it", "the", "of", null]
n = 3

"-"
a = ["it", "the", null, null]
n = 2

"-"
a = ["it", null]
n = 1

"it"
a = ["it", "it"]
n = 2

"was"
a = ["it", "it", "was", null]
n = 3

"-"
a = ["it", "it", null, null]
n = 2

"the"
a = ["it", "it", "the", null]
n = 3

"-"
a = ["it", "it", null, null]
n = 2

"-"
a = ["it", null]
n = 1
"""
