def main():
    s = input("How are you feeling Baby Girl: ")
    st = convert(s)
    print(st)


def convert(string):
    st = string.replace(":)", "😊").replace(":(", "😒")
    return st


main()
