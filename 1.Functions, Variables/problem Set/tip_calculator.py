def main():
    rupees=rupees_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip=rupees*percent
    print(f"Leave Rs.{tip:.2f}")

def rupees_to_float(d):
    s=d.replace("Rs.","")
    return float(s)

def percent_to_float(p):
    return float(p)/100

main()