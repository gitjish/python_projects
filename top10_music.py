import requests
from bs4 import BeautifulSoup

baseurl = "https://www.billboard.com/charts/hot-100/"
input_date = input(
    "Which date would you like to choose in format yyyy-mm-dd 2000-08-12 "
)
response = requests.get(baseurl+input_date)
# print(response)
billboard_html = response.text
# print(billboard_html)

soup = BeautifulSoup(billboard_html, 'html.parser')
# print(soup)
song_name = soup.find_all(name="h3", class_="a-no-trucate")
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]

song_title = [song.getText().strip() for song in song_name]
print(song_title)
#for i in song_title:
    #print(i)

#with open("movies.txt", mode="w") as file:
#for song in songs:
#file.write(f"{song}\n")
 #h3_content = soup.find_all(
#     name="h3", class_="mega-menu-item-heading lrv-u-flex lrv-u-align-items-center lrv-u-color-white u-border-b-2@desktop lrv-u-border-color-brand-primary a-become-color-white-on-expand")
# print(h3_content)
#70f3d3f947aa412b8781c3393105d504
#aee222c628f6400e99b66db63c172f7f
#client_id=28faef88c6074afa9c046eeb09a4bd0b
#client_secret=2648ee4483984721abe5fe9c19564d66
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="28faef88c6074afa9c046eeb09a4bd0b",
                                               client_secret="2648ee4483984721abe5fe9c19564d66",

                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               redirect_uri="https://example.com",
                                               cache_path="token.txt")

        
        
    )

user_id = sp.current_user()["id"]


results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
