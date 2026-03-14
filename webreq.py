import requests as req
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = req.get(url)

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.select(".storylink")

for i, headline in enumerate(headlines[:10], 1):
    print(f"{i}. {headline.text}")


import csv

with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Rank", "Headline"])
    for i, headline in enumerate(headlines[:10], 1):
        writer.writerow([i, headline.text])
