# Below we learnt properties ,getter and setter in python.
class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # getter and setter for "name" instance variable -->
    @property  # ---> getter
    def name(self):
        return self._name

    # above we just created a property named "name"

    # why @name.setter?  ---> cause we just created a property named "name".So, for this "name"
    #                         property we want to create a setter.
    @name.setter  # ---> explicitly making the setter
    def name(self, name):
        if not name:  # ---> means name!=none
            raise ValueError("name is not given")
        self._name = name

    # getter and setter for "roll_no" instance variable -->
    @property  # ---> getter
    def roll_no(self):
        return self._roll_no

    @roll_no.setter
    def roll_no(self, roll_no):
        if roll_no not in range(1, 60):
            raise ValueError("Roll NO not in range")
        self._roll_no = roll_no

    # after making getter and setter for "name" and "roll_no" ,name of our instance variable changed
    # to "_name" , "_roll_no" and "name" and "roll_no" becomes a property.
    # So when you do self.name --> meaning you are calling property and,
    # if you do self._name ---> meaning you are calling instance variable.
    # That means instance variable name changed to _name and _roll_no
    def __str__(self):
        return f"{self.name}--->{self.roll_no}"


def main():
    Student = get_student()
    # Student._name = "" ---> no exception raised
    # Student.name = "" ----> exception raised
    print(Student)


def get_student():
    name = input("Name: ")
    roll_no = input("Roll No.: ")
    return student(name, roll_no)


if __name__ == "__main__":
    main()


# Notes --->
"""
1) See above , __init__ is same as before no change.
2) Now the real catch is the getter and setter we made for name and roll_no instance variable.
3) In previous programs of this oops we made classes in which we created instance variable inside
   the classes and using __init__ assaign them but any programmer can change these variables from
   even outside the class using '.' operator and can add value that is not accepted by me
   .So, what can we do. For this purpose we make getter and setter here.

4) @syntax is used to make getter and setter.
   @property define the getter 
   @<variableName>.setter ---> defines setter

5) "getter" and "setter" function needs to be the same name as the instance variable it is for.

6) Look for the further explanation in my notebook.

5) There are no access modifiers like private, public ,protected in python instead in python
    to tell someone that donot access or change this variable's value just put 1 "_" before the name
    of that variable. Ex ---> _house , _name etc.

    And if the you doesnt want "strongly" that anybody change the instance variable value, than you
    put 2 "_" before the name of the variable . Ex ---> __house, __name etc.

    That means we just trust other programmers to not change the variable name because in python 
    there are no private or public modifiers.
"""
