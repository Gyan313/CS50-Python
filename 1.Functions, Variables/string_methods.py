name=input("enter your name : ")

# if you want to wrap all the things in one line
# name=input("enter your name : ").strip().title()

# remove white spaces from strings
name = name.strip()

# capatalize the 1st letter of string
name=name.capitalize()

# capitalize the every words 1st letter in a string
name=name.title()

first,second= name.split(" ")

# print string
print(f"Hello ,{first}")