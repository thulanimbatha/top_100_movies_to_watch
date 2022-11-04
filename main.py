import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
web_contents = response.text

soup = BeautifulSoup(web_contents, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
movie_list = []

for movie_title in movie_titles:
    movie = movie_title.get_text()
    movie_list.append(movie)

print(movie_list)
