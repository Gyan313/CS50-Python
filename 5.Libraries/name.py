import sys
 
def main1():
    if(len(sys.argv)<2):
        sys.exit()
    elif len(sys.argv)>2:
        sys.exit("too many arguments")

    print("Hey there i am",sys.argv[1])
# main1()


# doing sys.argv list slicing
def main2():
    if len(sys.argv)<2:
        print("too few arguments")
    
    for arg in sys.argv[:-2]:
        print(arg)
main2()