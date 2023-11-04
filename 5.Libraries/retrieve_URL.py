# Our aim to get tracknames for a particular artist (given by user as terminal argument) from
# the itunes(Apple)..

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()  # exit from whole program

# requests.get ---> get you the json text from the url provided
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1]
)

# parsing the json text we got from the url to make it more readable...
print(json.dumps(response.json(), indent=2))

j = response.json()

# 'j' is a dictionary like below example.
for result in j["results"]:
    print(result["trackName"])


# Example of output:::::

""" PS C:\Users\GYAN\Desktop\PYTHON Programming\CS50 Intro to Python> python -u "c:\Users\GYAN\Desktop\PYTHON Programming\CS50 Intro to Python\5.Libraries\retrieve_URL.py" "Ed sheeran"

{
  "resultCount": 5,
  "results": [
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 307958707,
      "collectionId": 911186468,
      "trackId": 911186476,
      "artistName": "Hoodie Allen",
      "collectionName": "People Keep Talking",
      "trackName": "All About It (feat. Ed Sheeran)",
      "collectionCensoredName": "People Keep Talking",
      "trackCensoredName": "All About It (feat. Ed Sheeran)",
      "artistViewUrl": "https://music.apple.com/us/artist/hoodie-allen/307958707?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/all-about-it-feat-ed-sheeran/911186468?i=911186476&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/all-about-it-feat-ed-sheeran/911186468?i=911186476&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/dd/85/25/dd85258c-95b7-52de-ecfe-f6af3d08ae99/mzaf_16624767521411984302.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/00/ca/8e/00ca8e18-c222-8712-9ddc-1ccd64952250/075679934574.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/00/ca/8e/00ca8e18-c222-8712-9ddc-1ccd64952250/075679934574.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/00/ca/8e/00ca8e18-c222-8712-9ddc-1ccd64952250/075679934574.jpg/100x100bb.jpg",
      "collectionPrice": 9.99,
      "trackPrice": 1.29,
      "releaseDate": "2014-10-13T12:00:00Z",
      "collectionExplicitness": "explicit",
      "trackExplicitness": "explicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 14,
      "trackNumber": 5,
      "trackTimeMillis": 205733,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Hip-Hop",
      "contentAdvisoryRating": "Explicit",
      "isStreamable": true
    },
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 159260351,
      "collectionId": 1589139584,
      "trackId": 1589139821,
      "artistName": "Taylor Swift",
      "collectionName": "Red (Taylor's Version)",
      "trackName": "Everything Has Changed (Taylor's Version) [feat. Ed Sheeran]",
      "collectionCensoredName": "Red (Taylor's Version)",
      "trackCensoredName": "Everything Has Changed (Taylor's Version) [feat. Ed Sheeran]",
      "artistViewUrl": "https://music.apple.com/us/artist/taylor-swift/159260351?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/everything-has-changed-taylors-version-feat-ed-sheeran/1589139584?i=1589139821&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/everything-has-changed-taylors-version-feat-ed-sheeran/1589139584?i=1589139821&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/15/c9/c8/15c9c8e3-5475-0e57-4981-c0f11e7ba171/mzaf_15579083659347135240.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e1/b1/04/e1b10422-f39c-a8c7-195b-ebdb8c05489c/21UM1IM25046.rgb.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e1/b1/04/e1b10422-f39c-a8c7-195b-ebdb8c05489c/21UM1IM25046.rgb.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e1/b1/04/e1b10422-f39c-a8c7-195b-ebdb8c05489c/21UM1IM25046.rgb.jpg/100x100bb.jpg",
      "collectionPrice": 14.99,
      "trackPrice": 1.29,
      "releaseDate": "2021-11-12T12:00:00Z",
      "collectionExplicitness": "explicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 30,
      "trackNumber": 14,
      "trackTimeMillis": 245423,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Pop",
      "isStreamable": false
    },
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 159260351,
      "collectionId": 1589139584,
      "trackId": 1589139887,
      "artistName": "Taylor Swift",
      "collectionName": "Red (Taylor's Version)",
      "trackName": "Run (Taylor's Version) [From The Vault] [feat. Ed Sheeran]",
      "collectionCensoredName": "Red (Taylor's Version)",
      "trackCensoredName": "Run (Taylor's Version) [From The Vault] [feat. Ed Sheeran]",
      "artistViewUrl": "https://music.apple.com/us/artist/taylor-swift/159260351?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/run-taylors-version-from-the-vault-feat-ed-sheeran/1589139584?i=1589139887&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/run-taylors-version-from-the-vault-feat-ed-sheeran/1589139584?i=1589139887&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/2d/e0/c7/2de0c760-e118-d131-22b0-77dad00f1c0e/mzaf_7793039678823145253.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e1/b1/04/e1b10422-f39c-a8c7-195b-ebdb8c05489c/21UM1IM25046.rgb.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e1/b1/04/e1b10422-f39c-a8c7-195b-ebdb8c05489c/21UM1IM25046.rgb.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e1/b1/04/e1b10422-f39c-a8c7-195b-ebdb8c05489c/21UM1IM25046.rgb.jpg/100x100bb.jpg",
      "collectionPrice": 14.99,
      "trackPrice": 1.29,
      "releaseDate": "2021-11-12T12:00:00Z",
      "collectionExplicitness": "explicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 30,
      "trackNumber": 28,
      "trackTimeMillis": 240223,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Pop",
      "isStreamable": false
    },
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 1539173328,
      "collectionId": 1596124746,
      "trackId": 1596124747,
      "artistName": "#Karma",
      "collectionName": "Ed Sheeran (Acoustic) [Acoustic] - Single",
      "trackName": "Ed Sheeran",
      "collectionCensoredName": "Ed Sheeran (Acoustic) [Acoustic] - Single",
      "trackCensoredName": "Ed Sheeran (Acoustic)",
      "artistViewUrl": "https://music.apple.com/us/artist/karma/1539173328?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/ed-sheeran-acoustic/1596124746?i=1596124747&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/ed-sheeran-acoustic/1596124746?i=1596124747&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview116/v4/b1/a8/81/b1a88132-3a9f-f9b9-f591-90d50ad7c310/mzaf_652824405154583626.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/fd/59/0c/fd590c18-fc67-e21f-2b57-57495b05682b/artwork.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/fd/59/0c/fd590c18-fc67-e21f-2b57-57495b05682b/artwork.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/fd/59/0c/fd590c18-fc67-e21f-2b57-57495b05682b/artwork.jpg/100x100bb.jpg",
      "collectionPrice": 0.69,
      "trackPrice": 0.69,
      "releaseDate": "2021-11-12T12:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 1,
      "trackNumber": 1,
      "trackTimeMillis": 145532,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Singer/Songwriter",
      "isStreamable": true
    },
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 183313439,
      "collectionId": 858512800,
      "trackId": 858517200,
      "artistName": "Ed Sheeran",
      "collectionName": "x (Deluxe Edition)",
      "trackName": "Thinking Out Loud",
      "collectionCensoredName": "x (Deluxe Edition)",
      "trackCensoredName": "Thinking Out Loud",
      "artistViewUrl": "https://music.apple.com/us/artist/ed-sheeran/183313439?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/thinking-out-loud/858512800?i=858517200&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/thinking-out-loud/858512800?i=858517200&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview116/v4/2f/e3/e1/2fe3e1b7-fa23-7df1-dba1-5b2d2be255f8/mzaf_14267287990353675224.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Features125/v4/a7/7b/92/a77b92fc-d331-dd1b-8772-80597dc51fd0/dj.xllwtvne.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Features125/v4/a7/7b/92/a77b92fc-d331-dd1b-8772-80597dc51fd0/dj.xllwtvne.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Features125/v4/a7/7b/92/a77b92fc-d331-dd1b-8772-80597dc51fd0/dj.xllwtvne.jpg/100x100bb.jpg",
      "collectionPrice": 12.99,
      "trackPrice": 1.29,
      "releaseDate": "2014-06-20T07:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 16,
      "trackNumber": 11,
      "trackTimeMillis": 281560,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Pop",
      "isStreamable": true
    }
  ]
}

----> Below are the tracknames we get....
All About It (feat. Ed Sheeran)
Everything Has Changed (Taylor's Version) [feat. Ed Sheeran]
Run (Taylor's Version) [From The Vault] [feat. Ed Sheeran]
Ed Sheeran
Thinking Out Loud
 """


# json.loads is used to convert a JSON string into a Python object, while json.dumps is used to convert a Python object into a 
# JSON string. These functions are commonly used when working with JSON data, especially in scenarios where you need to read or 
# write data to/from a JSON format, such as when working with web APIs or configuration files.