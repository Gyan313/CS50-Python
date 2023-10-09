import pyfiglet
from random import choice
import sys


def main():
    txt = input("Input: ")
    fontList = pyfiglet.FigletFont.getFonts()
    ranFont = choice(fontList)

    if len(sys.argv) == 1:
        print("Output:", pyfiglet.figlet_format(txt, font=ranFont))

    elif (sys.argv[1] != "-f" or sys.argv[1] != "--font") or sys.argv[
        2
    ] not in fontList:
        print("Invalid usage")
        sys.exit()

    else:
        print("Output:", pyfiglet.figlet_format(txt, font=sys.argv[2]), sep="\n")


main()
