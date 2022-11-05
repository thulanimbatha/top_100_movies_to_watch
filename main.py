import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
web_contents = response.text    # get the text

soup = BeautifulSoup(web_contents, "html.parser")   # make soup
# search and find all movie titles
movie_titles = soup.find_all(name="h3", class_="title")
movie_list_copy = []
# add each title to the list
for movie_title in movie_titles:
    movie = movie_title.get_text()
    movie_list_copy.append(movie)
movie_list = movie_list_copy[::-1]  # reverse the list

# write to file
with open("./movies.txt", "w", encoding="utf8") as movie_file:
    for movie in movie_list:
        movie_file.write(f"{movie}\n")

