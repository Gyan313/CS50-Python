""" 
# how "\r" works

The "\r" escape sequence is used to move the cursor back to the beginning of the line 
before printing the updated progress.

When running this code, you will see the progress being updated on the same line 
without creating new lines, giving the illusion of an updating progress indicator. 
The final message "Process complete!" is printed after the loop finishes executing.

import time

for i in range(10):
    print(f"Progress: {i}/10", end="\r")
    time.sleep(1)

print("Process complete!")
# "\r\n" simply means newline

"""


# use binary mode to read or write in a program or image file, any non-text data file.
with open("Last_program.py", "r+b", buffering=1) as file:
    print(file.readlines())


# Buffering parameter notes ---->

# However, the `open()` function does accept an optional `buffering` parameter, which determines
# the buffering policy to be used for the file. The `buffering` parameter controls how much data
#  is read from or written to the file at once.

# If the `buffering` parameter is not specified or set to `-1`, the default buffering policy is
#  used. This typically means that the file is buffered according to the system default.

# You can also specify different buffering options:
# - If `buffering` is set to `0`, it means no buffering is performed, and each read or write
# operation directly accesses the file.
# - If `buffering` is set to `1`, line buffering is used. This means that the file is buffered by
#  line, and each write operation is written to the file immediately.
# - If `buffering` is set to any positive integer greater than `1`, it specifies the buffer size
#  in bytes. In this case, the file is buffered with the specified buffer size.

# Here's an example of using the `buffering` parameter with the `open()` function:


# # Buffered I/O with a buffer size of 4096 bytes
# with open('file.txt', 'r', buffering=4096) as file:
#     # Perform read/write operations on the file

# Remember, if you don't explicitly specify the `buffering` parameter, the default buffering
#  behavior will be used, which is generally recommended in most cases.


# using rstrip() method of string.

# name = "gyan....qyllllyqqq,,,,,"
# print(name.rstrip(".,qyl"))

with open("filename", "r") as file:
    for line in sorted(file):
        print(line)
