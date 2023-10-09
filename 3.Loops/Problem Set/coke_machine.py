def main():
    amt=int(input("Amount due: "))

    while True:
        InsertCoin=int(input("Insert coin: "))
        if(InsertCoin==25 or InsertCoin==10 or InsertCoin==5):
            if (InsertCoin)<amt:
                amt=amt-InsertCoin
                print("Amount due:",amt)
            else:
                print("Change Owed:",InsertCoin-amt)
                break

main()
    