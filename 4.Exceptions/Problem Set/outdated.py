def main():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    Dict={}
    n=1
    for i in months:
        Dict[i]=n
        n+=1
    getDate(Dict,months)

def getDate(Dict,months):
    while True:
        try:
            date=input("Date: ")
            if "/" in date:
                month,day,year=date.split("/")
                if(int(month)>0 and int(month)<13) and (int(day)>0 and int(day)<32):
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
            if " " in date:
                date=date.replace(",","")
                month,day,year=date.split(" ")
                if month.isdigit()==False and month in months and len(year)==4:
                    print(f"{year}-{Dict[month.title()]:02}-{int(day):02}")
                    break
        except (ValueError,TypeError,EOFError):
            print()
            pass

main()
        