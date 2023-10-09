Students = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Harmaioni", "house": "Griffindor"},
    {"name": "Ron", "house": "Griffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


# Below written code creates a list of all houses from above Students list in the houses list
# below.
def main():
    houses = []
    for student in Students:
        if student["house"] not in houses:
            houses.append(student["house"])

    for house in sorted(houses):
        print(house)


main()
# But we can use "set" in python to "remove duplicates" just like above but with a short code
# See below


def main1():
    houses = set()
    for student in Students:
        houses.add(student["house"])

    # set() is just like "list", a container
    for house in sorted(houses):
        print(house)

    # The major advantage of using a set, as opposed to a list, is that it has a highly optimized
    # method for checking whether a specific element is contained in the set. This is based on a
    # data structure known as a hash table. Since "sets are unordered", we cannot access items using
    # indexes as we do in lists.

    # but you can access elements of set() using for loop, like we did above.


main1()
