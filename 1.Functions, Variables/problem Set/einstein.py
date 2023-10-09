def main():
    m=int(input("m: "))
    energy(m)

def energy(mass):
    E=mass*(300000000**2)
    print(f"E: {E}")

main()