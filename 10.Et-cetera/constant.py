GYAN = 2  # ---> constant variable in python
# Here GYAN is global too.

# Constant variable characteristics in python:
# 1) Constant variable has to have only capital words by convention.Than that variable will be
#    considered as constant variable by python we donot need to do anything else to make a variable constant in python.
# 2) But constant variable in python can be changed after initializing it, python doesnt strongly enforce this.
# 3) Means naam ka constant h ye variable , it is not like if we change its value python's gonna
#    give us error.

GYAN = 9  # --> value of constant variable "GYAN" is changed to 9.

for i in range(GYAN):
    print("gyan")


# how to use and access "constant variable" in class
class Cat:
    MEOW = 6

    def meow(self):
        # to access constant variable in python access it like a class variable, using classname and '.' notation
        # like below Cat.MEOW
        for _ in range(Cat.MEOW):
            print("Meow")


cat = Cat()
cat.meow()
