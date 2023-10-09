# class methods and static methods are 2 slightly different method in python.
# "class methods" :  is commonly used when you want to define methods that operate
# on the class itself,rather than on specific instances.

import random


class Movie:
    location = ["G3X", "M2K", "Pashim Vihar", "Janak puri"]

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("movie name not provided")
        self._name = name

    @property
    def house(self):
        return self._duration

    @house.setter
    def house(self, duration):
        if duration > 200:
            raise ValueError("Exeeding time limit")
        self._duration = duration

    def __str__(self):
        return f"{self.name} and {self.duration}"

    @classmethod  # --> @ syntax used here to intialize below method as class method.
    # above @syntax is must, when declaring a class method without it error occures.
    def MovieHall(cls):
        print(f"Location of the movie ---> {random.choice(cls.location)}")

    # See in above method we use "cls" instead of "self" due to above fucntion is a class
    # method that means "self" cannot be used in it cause "self" denote the reference of
    # current object accessing the fucntion but class method do donot depend on the object
    #  and thus not accessed using object of the class ,thats why we dont use
    # "obj." notation to access them .Thats why developers of python developed "cls" that
    # references to the class instead of the object. Here location is the class variable.

    @classmethod
    def newObj(cls):
        name = input("Name: ")
        duration = int(input("Duaration: "))
        return cls(name, duration)
        # --> we used "cls" here to make a new object. As cls refers to the class we are in.
        # you can also do ---> return Movie(name,duration)


def main():
    # We are creating object of Movie class outside of the class below. But there is a way
    # using class methods, we can create a function in the Movie class itself that makes
    # new object for us like below when called. Check above.
    # Basically we want to encapsulate everything related to class inside the class we have.
    """
    name = input("Name: ")
    duration = int(input("Duaration: "))
    movie = Movie(name, duration)
    """

    movie = Movie.newObj()  # ----> movie contains a new obj of Movie class
    print(movie)
    Movie.MovieHall()  # --> accessing the class method.
    #                        This shows that class method do donot re-intialized with a
    #                        every new object but rather it remians same valued
    #                        for all the object of class.
    # Thus class method and class variable has a lifetime of program.


if __name__ == "__main__":
    main()


# If your program has a __init__() method and a class method and if you call class method
# than your __init__() method will not be called with the class method cause
# remember __init__() is there to initialize the instance variable of the class that means
# it initialize with every new obj.
