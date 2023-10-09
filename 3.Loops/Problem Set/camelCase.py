def main1():
    string=input("Camel_case: ")
    l=[]
    n=0

    for i in range(len(string)):
        if string[i].isupper():
            l.append(string[n:i])
            n=i
    l.append(string[n:len(string)])
    
    str1=""
    for i in range(len(l)):
        if i==(len(l)-1):
            str1+=l[i]
            break
        str1+=l[i]+"_"

    print("snake_case:",str1.lower())
# main1()

# 2nd way to solve this code
def main2():
    string=input("Camel_Case: ")

    text=""
    for i in range(len(string)):
        if string[i].isupper():
            text=string.replace(string[i],"_"+string[i].lower())
        text+=string[i]
    print("small_case:",text)
# main2()

# 3rd way
def main3():
    string=input("Camel_Case: ")
    
    print("snake_case: ",end="")
    for i in string:
        if i.isupper():
            print("_"+i.lower(),end="")
            continue
        print(i,end="")
main3()