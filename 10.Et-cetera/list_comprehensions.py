# It is a pythonic way to make list on fly.
# By using list comprehensions we can make lists in one line elegently, without using for loop
# or any list functions.


# Write a list containing all the upper case words of the given sentence.
def main():
    yell("my", "name", "is", "gyan")


def yell(*words):
    uppercase = [word.upper() for word in words]
    # [word.upper() for word in words] --> this is one example of list comprehension.
    print(*uppercase)


# main()


# List conprehension with conditions
def main1():
    Team = [
        {"name": "gyan", "topic": "S"},
        {"name": "dev", "topic": "S"},
        {"name": "Hemant", "topic": "W"},
        {"name": "navneet", "topic": "O"},
    ]

    S = [student["name"] for student in Team if student["topic"] == "S"]
    # see above we applied if condn

    for s in S:
        print(s)

    # What we did in this main1() can also be done using filter in python.


main1()
