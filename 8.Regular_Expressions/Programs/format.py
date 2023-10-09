# Formating the users input using Regex
# In this program we are going to format the users inputed name.In a way which we want.

import re


def main():
    name = input("Enter your name: ").strip()
    """
        There are 2 formats of name people may type--->
        1) without comma ----> means first word is the first name and second word is the second name    
                                eg. "Gyan Dev" --> this is the way we want users name 
        
        2) with comma ----> means before comma last name and after comma first name
                            eg. (Dev, Gyan) OR (Dev,Gyan)

    """
    matches = re.search(r"(.+) *, *(.+)", name)
    # "matches" only contain something if name has comma.matches is a list.
    # that means without comma no if condn is executed as matches will be "empty"== false.
    # matches is a object.That contains groups of the string we want to search in a user inputed string,it detacts group by
    # using (...) we gave in regex.
    if matches:
        last = matches.group(1)  # group is a function in re module
        first = matches.group(2)
        name = f"{first} {last}"
    print(name)

    # see above r"(.+) *, *(.+)" --> contains 2 groups (.+), one before comma and other after comma
    # matches.group(0) ---> exact string user entered with comma.

    # (space)* means space can be 0 or more. It is same if you do last.strip() and first.strip()


main()


# Lets tighten things up in the above code
def main1():
    name = input("Enter your name: ").strip()

    if matches := re.search(r"(.+) *, *(.+)", name):
        name = matches.group(1) + " " + matches.group(2)
    print(name)

    # See in above code " := " ---> this "walrus operator".
    # Use of walrus operator :
    #     It is used when you want to assaign a variable along with using that variable for boolean
    #     purposes like in if and elif conditions.


main1()
