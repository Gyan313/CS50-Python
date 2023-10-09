
# 1st way
def main():
    print_grocery()

def print_grocery():
    Items=[]
    while True:
        try:
            Grocery=input().lower()
            Items.append(Grocery)
        except (ValueError,TypeError,NameError):
            pass
        except EOFError:
            break
    print()
    d={}
    for i in Items:
        n=Items.count(i)
        if i not in d:
            d[i.upper()]=n
    for i in d:
        print(d[i],i)
# main()

# 2nd way
def main1():
    print_grocery()

def print_grocery():
    Items=dict()
    while True:
        try:
            Grocery=input().lower()
            if Grocery in Items:
                Items[Grocery]+=1
            else:
                Items[Grocery]=1
        except (ValueError,TypeError,NameError):
            pass
        except EOFError:
            print()
            for i in Items:
                print(Items[i],i.upper())
            break
main1()

