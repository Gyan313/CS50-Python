# Validating the users input using Regex

import re

# VERY VERY important stuff must go to the docs of re module you will learn a lot.

# (https://docs.python.org/3/library/re.html)
# Go on above link to look at the "re module" python doc.


def main():
    email = input("enter your email id: ")

    if re.search("@", email):
        print("valid")
    else:
        print("not valid")

    """ 
        This "re.search" function search the @ in the whole email
        we inputed but the problem is it's gonna give the output
        valid even when user just input @.gyan
    """


# if __name__=="__main__":
# main()

""" 
    to solve above problem we need to use search() function's pattern paramter.
    Now pattern parameter can take some special characters which mean something 
    particular in pattern recognition.To know those special characters look in 
    notes on the notes copy.😎 
"""


def main1():
    email = input("enter your email id: ")

    if re.search(".*@.*", email):  # ".*" means something to the left and on right
        print("valid")
    else:
        print("not valid")

    """ 
        ---> Still we are going to get valid for invalid email, but i guess
        this program much better than prev program.

        ---> If you give input here "@" output will be valid same as above 
             program but we use "special char" here than why same output??
             cause '*' mean 0 or more characters. Matlab 0 char is also fine.
             So, this is the problem.

    """


# main1()

""" 
    To resolve upper problem ,I propose we use a "+" instead of "*" as 
    "+" means (1 or more characters) here 1 is important means you cant give 0
    char before and after "@".
"""


def main2():
    email = input("enter your email id: ")

    if re.search(".+@.+", email):  # "." means any char except '\n'
        print("valid")
    else:
        print("not valid")

    """
        If you dont want to use "+" what else can we do????

            Ans))Do this ----> re.search("..*@..*")
                cause here '.' means any char("one" precisely) and '.*' means 0 or more characters . Same result as "+".
    """


# main2()


def main3():
    email = input("enter your email id: ")

    if re.search(r".+@.+\.com", email):
        print("valid")
    else:
        print("not valid")

    """
        Look closely in above program ,check search function, you will see 2 new
        characters "r" and "\", what do they used for??
         
        : "\" --> backslash is used above or in regular expressions so that char 
                  after backslash treated as a string to be matched literally not a special
                  symbol like *,+,. etc.
                  Above we use "\" so that . in .com is not recognised by python as
                  special symbol of search function as we discused earlier.

        : "r" --> is used to specify a string as "raw string".
                    Go to this website "https://www.codevscolor.com/python-raw-string" to learn about raw string.
                When we used raw string above, backslash "\" is not treated as special char in python


        Now if the inputed email by user doesnt contain (.com) than our program gives output "Invalid".

        --> However there is still a problem that is'nt solved yet, what if  someone enter a lot of '@' in the inputed email.
        Ex... email= gyan.2102@@@@@@@gmai.com  here the answer will be valid.
            So now we need to solve this problem.
    """


# main3()


"""
    what if someone enters "a whole sentence" that contains a "@" and ".com" in main3() function email.      Ex---> email="My name is Gyan.2003@gmail.com.".
    What do you think what will happen??
    The answer will be Valid but the email entered is Invalid as we know, so how can we improve our above code to return answer Invalid to us.
"""


def main4():
    email = input("enter your email id: ")

    if re.search(r"^.+@.+\.com$", email):
        print("valid")
    else:
        print("InValid")

    """
        Look at "re.search(r"^.+@.+\.com$",email)" .Here you can see '^' and '$' 
        ,these are 2 special symbols in regular expressionss.

        What does these special char means???
        Ans) 
            '^' --> It is called "carrot". "Matches the start of the string to be
                    seached".

            '$' --> matches the end of the string to be searched or just before
                    the newline at the end of the string.


        --> So, now when you entered the whole sentence.
            Ex. --> email="My name is Gyan.2003@gmail.com."
            Answer will be "Invalid".

            But did you understood why ans is invalid??
                Because see at the end of example sentence you will see the '.'
                fullstop but we gave '$' just after .com means there have to be 
                no char after '.com' but every sentence ends with a fullstop so 
                passed sentence will be Invalid.

                That means if no fullstop is passed the above sentence answer will be "valid" , i mean yess.
    """


# main4()


"""
    If user pass multiple @ in the email, our answer is still "valid". So, what do we do now??
    I guess its time to introduce you with new special char,which are-->

        i) [] --> allows you pass set of characters, which are the only character 
                  that can be present at a particular pos. in  the email.

        ii) [^] ---> allows you pass which set of character cant be at a          particular position in the email.
"""


def main5():
    email = input("enter your email id: ")

    if re.search(r"^[^@]+@[^@]+\.com$", email):
        print("valid")
    else:
        print("Output: InValid")

    """
        In above "re.search(r"^[^@]+@[^@]+\.com$",email)" we removed '.' before
        "+" and added a [^@].

        [^@] --> it means our inputed email from user cannot have "@" before a  
                 @ and and after the @ that means email can have any char(a-z,A-Z,0-9)
                 but cannot have @ due to we gave a little carrot(^) in [^].

        But now user cannot input a email with lots of @. "Hurray!!😎"
    """


# main5()

# going more close to get the email check right.


def main6():
    email = input("enter your email id: ")

    if re.search(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9_]+\.com$", email):
        print("valid")
    else:
        print("Output: InValid")

    """
        1) You can give range in [] ,you dont have have to write all the char or 
           numbers you want inside [].
        2) How to give ranges check up, above [] are with no '^' that means you
           can involve only these char in you email ,aage and peeche of @.
        3) You dont have to give any spaces,commas and anything in b/w different
            ranges inside [].
    """


# main6()

# What we did up with [ranges] was a little cryptic , so to shorten that up python
# provides us with some special characters(escape Sequence).

# Escape Sequence --> an escape sequence is a combination of characters that has
# a meaning other than the literal characters contained therein.


def main7():
    email = input("enter your email id: ")

    if re.search(r"^\w+@\w+\.com$", email):
        print("Output: Valid")
    else:
        print("Output: Invalid")

    """
        1) "\w" replaced whole "[a-zA-Z0-9_]" ---> look carefully it doesnt contain "."  
            Here "\w" ----> means all the words, numbers and "_" too and not
            anything else.
        2) There are lot more of these special characters containing backslash
            like "\w" and they can make our life easier with patterns which are
            so common like ranges a-z,A-Z,0-9 etc. .Read them in notebook.
    """


# main7()


def main8():
    email = input("enter your email: ").strip()

    if re.search(
        r"^\w+@\w+\.(edu|com|gov|io|in)$", email, re.IGNORECASE
    ):  # ---> here,you can group any strings together by using () brackets
        print("valid")
    else:
        print("Invalid")

    # (edu|com|gov|io|in) ---> '|' means "or", it is here to show that one can put any one of these domain name in their email

    # you can use | for grouping the strings and special symbols too.
    # eg. --> (r"^(\w|\s)+@\w+\.(edu|com|gov|io|in)$") ---> here (\w|\s) means any char(\w) or white space(" ").

    # You see above "re.IGNORECASE", this is the flag in the re.search() method and it is used to
    #  to ignore case(lower or upper) of the string to be checked against regular expressions.


# main8()


def main9():
    email = input("enter your email: ").strip()

    if re.search(
        r"^\w+(\.\w+)*@\w+(\.\w+)*\.(edu|com|gov|io|in)$", email, re.IGNORECASE
    ):
        print("valid")
    else:
        print("Invalid")

    # r"^\w+(\.\w+)*@\w+(\.\w+)*\.(edu|com|gov|io|in)$" ----> this regex accepts email with 0 or more dots on each side of the @.

    # (\.\w+)* ---> due to this regex we can have 0 or more dots on each side of the @

    # (\.\w+)? ----> if you add this in place of (\.\w+)*, here ? means 0 or 1 repetition.


main9()

""" 
^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9]
 (?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$ 


 ---> this is the regex that browser use to check the email address,it is still not the bestest 
      version but good enough.

    As we can see how crazy difficult to understand upper regex, thats why there are libraries in 
    python to do the searching for us.
"""

# re.match(pattern,string,flag=0) ---> starts matching your passed string from the very begining
#      of the string, so you dont need need to pass ^ to specify the starting of the string.
#      That means it works same as re.search() with a little difference.

# re.fullmatch(pattern,string,flag=0) ---> same as re.search() just here you dont need to specify
#                 in the regex where the string starts (^) and where it ends($).
