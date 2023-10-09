from typing import Any


def main():
    student = get_student()

    print(f"{student.name} - {student.age}")


class Student:
    ...
    # (...) a special literal that represents a placeholder or a marker.
    #  It is typically used in certain contexts to indicate that additional code or
    #  functionality needs to be added.
    # this special literal is here to show that class cant be empty, it needs to contain something.


def get_student():
    student = Student()
    student.name = input("name: ")
    student.age = input("age: ")
    # above name and age will be added in class Student.This is the way to make member variable
    # in class
    return student


# main()


# Classes and object ,constructor and instance variables -->


def main1():
    Movies = get_movies()

    print(Movies)


class movies:
    # Below written function is how you make constructor in python class.
    # self == (this) in c++
    # self --> is must always gonna be in every funtion's parameter in classes of python,
    #          so that calling object can access the function.
    # Below is a parameterized constructor.
    def __init__(self, name, duration):
        if not name:  # making sure name is not blank or none
            raise ValueError("Missing Name")
        if duration < 100 or duration > 200:
            raise ValueError("duration out of range")
        self.name = name
        self.duration = duration

    # "raise" is used to raise exception when you needed, you can use (try-except) block to
    # handle raised exception too.
    # "raise" can let you pass your message in the paranthasis of the exception, this way you
    # dont need to try understand what python interpreter say.
    # Ex --> raise ValueError("duration out of range")
    # Fun Fact --> you can make your own exceptions using raise keyword.
    # ex ---> raise gyanError("NO I don't fucking stop!! I get up again and again and again")

    def __str__(self):
        return f"{self.name} and {self.duration}"

    # You can either use above __str__ dunder method to print the instance variable of a object automatically(means no need for calling str to use str)
    # OR
    # Use a "display function" not built in python (not a magic func), made by me. Can called automatically
    # Result is gonna be the same with both but just calling the function using object is different.
    # Ex----> 1) __str__ ---> print(obj);  ---> str called automatically
    #         2) display() ----> print(obj.display())
    def display(self):
        return f"{self.name} and {self.duration}"


def get_movies():
    name = input("Name: ")
    duration = int(input("duration: "))
    return movies(name, duration)  # ---> returning the object of the class movies


main1()
