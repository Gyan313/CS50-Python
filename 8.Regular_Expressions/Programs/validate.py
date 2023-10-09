# validating email without using regualar expression
# without the use of regular expressions

email=input("What's your email?").strip()

if "@" and "." in email and email.endswith(".com"):
    print("Valid")
else:
    print("Not Valid")