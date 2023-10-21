def main():
    Future = {
        "Gyan Dev": "Tech-Entrepreneur",
        "Srishti Sharma": "IAS Officer",
        "Usha Sharma": "Artist",
        "other": "I dont care",
    }

    # print(Future)

    print(Future["Gyan Dev"])
    print(Future["Srishti Sharma"])
    print(Future["Usha Sharma"])
    print(Future["other"])

    for f in Future:
        print(f, Future[f], sep=" - ")


main()
