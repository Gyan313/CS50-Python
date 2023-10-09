# program


def main():
    time = input("What time is it?")

    time_hours = convert(time)

    if 7 <= time_hours <= 8 and time.endswith("am"):
        print("breakfast time")
    elif 12 <= time_hours <= 13 and time.endswith("pm"):
        print("lunch time")
    elif 18 <= time_hours <= 19 and time.endswith("pm"):
        print("dinner time")
    else:
        pass


# basically converting the time we get from user to completely in hours.
# Ex ---
# convert(7:30) ----> 7.5
def convert(time: str) -> float:
    hr, min = time.split(":")
    min_to_hr = int(min[:-2]) / 60
    # min[:-2] ---> "-2" means last se 2 char nahi needed hain.
    return int(hr) + min_to_hr


if __name__ == "__main__":
    main()
