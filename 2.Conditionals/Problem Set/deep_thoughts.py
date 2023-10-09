# Ques 1)

# Solution
# By using the regex in the python

import re

answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)

if re.search(r"[42]|forty(-| )two", answer):
    print("Yes")
else:
    print("No")
