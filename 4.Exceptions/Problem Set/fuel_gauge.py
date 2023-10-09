def main():
    fraction=take_input()
    output=get_output(fraction)
    print(output,"%",sep="")

def take_input():
    while True:
        try:
            f=input("Fraction: ")
            x,y=f.split("/")
            num=int(x)/int(y)
            return num
        except ValueError and ZeroDivisionError:
            pass

def get_output(fraction):
    f=fraction*100 
    if f<=1:
        return "E"
    elif 1<f<99:
        return round(f)
    else:
        return "F"
    
main()