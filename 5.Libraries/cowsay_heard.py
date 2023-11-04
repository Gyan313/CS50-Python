import cowsay,sys
# import sys

if len(sys.argv)==2:
    cowsay.cow("Hello, "+sys.argv[1])


# Example of output....
""" 
PS C:\Users\GYAN\Desktop\PYTHON Programming\CS50 Intro to Python> python .\5.Libraries\cowsay_heard.py gyan
  ___________
| Hello, gyan |
  ===========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     || 
"""