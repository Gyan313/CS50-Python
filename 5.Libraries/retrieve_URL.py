import requests
import sys
import json

if len(sys.argv)!=2:
    sys.exit()    # exit from whole program

response=requests.get("https://itunes.apple.com/search?entity=song&limit=5&term="+sys.argv[1])
print(json.dumps(response.json(),indent=2))

j=response.json()
for result in j["results"]:
    print(result["trackName"])



