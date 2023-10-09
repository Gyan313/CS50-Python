import sys
import datetime
import re
import calendar
import inflect  # ---> by pip install inflect

# "inflect" library is here to convert numbers to words and we can also remove "and" from the ouput string
# using inflect functionality.

# "calender" has a method calender.isleap() to check if year passed is leap or not.


# The fromisoformat() function is used to constructs a date object from a specified
# string that contains a date in ISO format. i.e., yyyy-mm-dd.
def main():
    dateOfBirth = get_DOB()
    # --> return the date of birth as list [year,month,day] and year,month and day are string.
    try:
        NewdateOfBirth = datetime.date(
            int(dateOfBirth[0]), int(dateOfBirth[1]), int(dateOfBirth[2])
        )
        # as dateOfBirth list contains all the elements string.
        # user can input a date like 0000-00-00 which is out of range of date.minyear.thats why i used
        # try-except block here
    except ValueError:
        print("Check your Newdateofbirth variable")
        sys.exit()

    currentDate = datetime.date.today()  # --> this gives you today's date

    TotalMinutesTillYouBorn = NumOfMinutes(NewdateOfBirth, currentDate)

    ig = inflect.engine()
    print(f"{ig.number_to_words(TotalMinutesTillYouBorn,andword='')}")


def get_DOB():
    DOB = input("Enter your DOB: ")
    check = re.search(r"(\d{4})-(0\d|1[0-2])-(0\d|[1-2]\d|3[0-1])$", DOB)

    # above regex can be = "([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$" too.
    # \d{4} ---> represent any digit with length 4
    # \d{1,2} ---> reperesent any digit with length 1 or 2.
    # \d = [0-9]
    if not check:
        print("Invalid Date")
        sys.exit()
    year = check.group(1)
    month = check.group(2)
    day = check.group(3)
    DOB = [year, month, day]
    return DOB


def NumOfMinutes(dateOfBirth, currentDate):
    # cannot do (currentDate - dateOfBirth).year --> produces error
    # same goes for (currentDate - dateOfBirth).month and (currentDate - dateOfBirth).day
    yearsOld = currentDate.year - dateOfBirth.year
    monthOld = abs(currentDate.month - dateOfBirth.month)
    daysOld = abs(currentDate.day - dateOfBirth.day)

    checkNumOfLeapYear = NumOfLeapYear(dateOfBirth, currentDate)

    NotLeapYear = yearsOld - checkNumOfLeapYear

    NotLeapYearInMinutes = NotLeapYear * 365 * 24 * 60

    LeapYearInMinutes = checkNumOfLeapYear * 366 * 24 * 60

    monthOldInMinutes = monthOld * 30 * 24 * 60
    daysOldInMinutes = daysOld * 24 * 60

    TotalMinutesTillYouBorn = (
        NotLeapYearInMinutes + LeapYearInMinutes + monthOldInMinutes + daysOldInMinutes
    )

    return TotalMinutesTillYouBorn


def NumOfLeapYear(dateOfBirth, currentDate):
    n = 0
    for i in range(dateOfBirth.year, currentDate.year + 1):
        if calendar.isleap(i):
            n = n + 1
    return n


if __name__ == "__main__":
    main()


# Above code can be shorten up,check out some github repos of this code
