class Marks:
    def __init__(self, marks):
        if marks < 0 or marks > 500:
            raise ValueError("Enter the right marks")
        self.marks = marks


class Sports:
    def __init__(self, points):
        if points < 0 or points > 10:
            raise ValueError("Enter the valid points")
        self.points = points


# Below is how we do Multiple inheretence and how we inherit base class in python
class Student(Marks, Sports):
    def __init__(self, marks, points):
        """
        Below using super() we are initializing initializing the base class variable
        But we can only use super() with one base class not multiple, if you use multiple super in __init__
        , it will just execute the 1st super() and going to skip the other super() below.

        super().__init__(marks)
        super().__init__(points) --> not gonna work

        """
        # ---> initializing the base class variables using sub-class.
        # we are accessing the baseclass methods using '.' operator
        # Belew is the format to access base class method when we have multiple base classes
        Marks.__init__(self, marks)
        Sports.__init__(self, points)
        self.agregate = ((marks + points) / 510) * 100

    def __str__(self):
        return f"Marks={self.marks} , sports={self.points} and Agregate={self.agregate}"

    @classmethod
    def newObj(cls):
        marks = int(input("Enter your total marks out of 500: "))
        points = int(input("Enter total points in sports out of 10: "))

        return Student(marks, points)


student = Student.newObj()
print(student)
