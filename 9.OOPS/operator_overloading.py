class Vault:
    def __init__(self, rupee=0, dollar=0, won=0):
        self.rupee = rupee
        self.dollar = dollar
        self.won = won

    # below __add__() is same as operator+()
    def __add__(self, other):
        rupee = self.rupee + other.rupee
        dollar = self.dollar + other.dollar
        won = self.won + other.won
        return Vault(rupee, dollar, won)

    def __str__(self):
        return f"Rupee = {self.rupee}, dollar = {self.dollar}, won = {self.won}"


gyan = Vault(100, 20, 1000)
print(gyan)
elon = Vault(100000, 32343353, 234342342352)
print(elon)
total = (
    gyan + elon
)  # ---> gyan + elon == gyan.__add__(elon) here self --> gyan and other ---> elon
print(total)
