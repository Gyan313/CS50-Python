# filter is exactly like map with just one difference that the function it takes needs to check
# every element of the iterator that it is true or not.
# Basically the container that filter returns is based on if fucntion returns true or false.

""" 
Synatx ---->
    filter(function, sequence)
Parameters:
    function: function that tests if each element of a 
    sequence true or not.
sequence: sequence which needs to be filtered, it can 
    be sets, lists, tuples, or containers of any iterators.
Returns:
    returns an iterator that is already filtered. 
"""


def main():
    Team = [
        {"name": "gyan", "topic": "S"},
        {"name": "dev", "topic": "S"},
        {"name": "Hemant", "topic": "W"},
        {"name": "navneet", "topic": "S"},
    ]

    Topic_S = filter(
        is_S, Team
    )  # --> here filter returns a list containing dictionary(a snippet of Team).

    for topic_filtered in sorted(Topic_S, key=lambda s: s["name"]):
        print(topic_filtered["name"])


def is_S(Team):
    return Team["topic"] == "S"


main()


# You can pass lamda functions in map and filter instead of creating a new function and than
# pass it.
