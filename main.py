import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
web_contents = response.text

soup = BeautifulSoup(web_contents, "html.parser")
print(soup.prettify())
