from bs4 import BeautifulSoup
import requests
from api_manager import ApiManager

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
music_tags = soup.select(selector="li ul li h3")
artist_tags = soup.select(selector="li ul li span")
musics = [tag.text.strip() for tag in music_tags]
artists = [tag.text.strip() for tag in artist_tags][::7]

playlist_name = f"Billboard Hot 100 When {date}"
manager = ApiManager()
playlist_id = manager.create_playlist(playlist_name)

track_ids = [manager.search_musics_id(music) for music in musics]
manager.add_musics_into_playlist(track_ids=track_ids, playlist_id=playlist_id)
