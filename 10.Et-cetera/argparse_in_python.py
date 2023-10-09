# Disciption: here we are gonna make command line "flags" and manipulate "flags" using argparse
# library.
# Ex of flags ---> "--help"

import sys


# sys.argv is a list that contains all the space seperated words or arguments you passed in command
# line after python ... ... ... on command line.
def main():
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        print("meow\n" * int(sys.argv[2]), end="")
    else:
        print("usage: argparse.py")


# main()

# So, when you use command line to execute the code, we sometime use flags to do specific things with
# the command we are using.
# See above we just made a new '-n' flag for our python <filename> command.

# But Heres a problem with above approach of making flags what if we try to make multiple flags
# not just one. What can we do than, cause the problem is now where in our sys.argv list we got those
# flags as they are scrambled in that list.So, we cant do what we did above.

# Solution to the above problem is "argparse" library.It is gonna

# How to use it? see below --->

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="Number of time cat meow", type=int)
# here type=int make our n variables's type int.
# default value of n=1.
args = parser.parse_args()

for _ in range(args.n):
    print("Meow")

# argparse is a library
# (argparse.ArgumentParser) is a class
# Explaination --->
"""
    PARSING ----> Analysing and interpreting the command line arguments according to
     some pre-defined rules.

    1) 1st we created an object named "parser" using argparse.ArgumentParser's construtor which 
       takes an argument called description.
       This object handles the commmand line parsing for your script. Now this parsed script
       returns a object that stored in parser variable.
       Now this object in parser has some methods.See below

    2) parser.add_argument("-n", help="Number of time cat meow", type=int)
        Here, add_argument() is a method of parser object which allows you to add individual arguments
        that your command line script will accept. Ex --> "-n" is a flag which we made and add to the 
        command line script of this program.

        "--help" is a flag which allows a user to see what are the functionality of a command.
        So, our add_argument() method provide us "help" parameter to tell what the added argument to 
        script can do or what are its functionality.

        So, if you do <prompt>python <path> -n <interger> --help than a list of functionality of -n argument 
        appears.
        We just created our very own custom made flag !!! how cool😊🙃!!!

    3)  When you call the parse_args() method on the argument parser object(parser variable), it 
        takes the input provided through the command line (typically as a list of strings) and applies the defined 
        rules to extract relevant information. It then returns an object that contains the parsed 
        values which in our case got stored in "args" variable.

    4) Now we recieved object in args when we do (args = parser.parse_args()). This args contains 
       all the parsed arguments or variable , so that we can use them in our code.Thats why we 
       can use (args.n).

"""

# What if someone entered the value of n string not int??
# ans)
#     usage: argparse_in_python.py [-h] [-n N]
#     argparse_in_python.py: error: argument -n: invalid int value: 'g'

# Meaning argparse library even provide us with error checking.


# IMPortant -->
# When you say import in Python, the interpreter runs a search to find a file with that name.
# It first looks for the file in the current folder and then in other paths.
# So, dont use same filename as your library name you are importing.
