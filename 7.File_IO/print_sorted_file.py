def main():
    with open("name.txt","r") as file:
        lines=file.readlines()

    for line in sorted(lines,reverse=True):    #reversing the names from file
        print("Hello,",line.rstrip())

if __name__=="__main__":
    main()