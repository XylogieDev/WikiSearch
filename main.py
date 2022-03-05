import requests
from bs4 import BeautifulSoup

topic = input("What topic would you like to search for? ")
response = requests.get("https://en.wikipedia.org/wiki/" + topic)
soup = BeautifulSoup(response.text, 'html.parser')

info = soup.find(class_="shortdescription nomobile noexcerpt noprint searchaux")
print(info.text)
