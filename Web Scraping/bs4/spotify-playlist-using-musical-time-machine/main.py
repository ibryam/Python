import requests
from bs4 import BeautifulSoup
import datetime as dt
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID="ajkakdjaslk;aslk;asl;akl;sjdl;askal;sdk"
CLIENT_SECRET="jkol;ajkl;asdjkl;asasdl;j0"
REDIRECT="http://example.com"

##########################################################################################################################################################################################
while True:
    date=input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD :")
    if len(date)==10:
        break
    print("Give correct date ")

year,month,day=date.split("-")


response=requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
songs=soup.select("div.chart-results li h3",id="title-of-a-story",class_="c-title")

songs=[song.getText().strip() for song in songs]


##########################################################################################################################################################################################

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="sdfsdfsdfsdfsfdzsdfsdfsdfsdfsdf",
    )
)
user_id = sp.current_user()["id"]



song_uris=[]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


param_playlist={
"name": f"{date} Billboard 100",
    "description": f"Top 100 songs from {date}",
    "public": "false"
}


playlist_url=sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description=f"Top 100 songs from {date}")



sp.playlist_add_items(playlist_id=playlist_url["id"], items=song_uris)
