# In this program we want our user to input a user name of twitter. But some users input
# there url instead
# So here we want to extract the username of twitter from a url.

import re

# Here we are gonna use a function from re library
# re.sub(pattern,repl,string,count=0,flag=0)  ---> structure of the (sub==substitute) function.
# pattern ---> to search in string
# repl ---> replacement of the pattern searched in the string
# string ---> on which we are searching and replacing
# count ---> how many times you want to find and replace


def main():
    url = input("URL: ").strip()

    # you can't write anything other than the below like url of twitter due to '^'
    # you cant input something like ---> "hey my account is https://twitter.com/gyan" dev.
    # "url" needs to start with https or www. or twitter
    username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    # username --> contains the extracted string

    print(username)

    # re.sub() cant help us if user write url of other website not twitter's.
    # So, we need to check that the website is of twitter's.
    # So we gonna use re.search().


# main()


def main1():
    url = input("URL: ").strip()

    # assuming domain name to be ".com" only.
    # twitters username can only contain [a-zA-Z0-9_] not anything possible so dont use "."
    stringMatched = re.search(
        r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+))", url, re.IGNORECASE
    )
    # see no $ is used in the end of the regex above
    # if condn to ensure the username is of twitter.
    # see above groups with (?:) is not included in stringMethod.group(1....)
    if stringMatched:  # if stringMatched empty( = none) false and otherwise true.
        print(f"Username: {stringMatched.group(1)}")
        # --> we have only 1 group that is capturing (above).by doing stringMatched.group(1)
        # we are getting the captured group which contain our username.

    # to understand above expression deeply go to the notes notebook.


main1()
