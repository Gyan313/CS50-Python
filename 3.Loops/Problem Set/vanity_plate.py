import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not(2<=len(s)<=6) or " " in s:
        return False
    if s[0].isdigit() or s[1].isdigit():
        return False
    for i in range(len(s)):
        if s[i] in string.punctuation:
            return False
        if s[i].isdigit():
            new=s[i:len(s)]
            break
    
    if new[0]=="0":
        return False
    for i in new:
        if not(i.isdigit()):
            return False
    return True
main()