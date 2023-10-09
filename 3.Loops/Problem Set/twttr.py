def main():
    tweet=input("Input: ")
    shorten_tweet=short(tweet)
    print("Output:",shorten_tweet)
    
def short(tweet):
    vowels=['a','e','i','o','u']
    twt=""
    for i in tweet:
        if i.lower() in vowels:
            continue
        twt+=i
    return twt

main()