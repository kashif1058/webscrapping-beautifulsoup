import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.amazon.com/s?k=iphone&crid=35HBVPQZF0OZJ&sprefix=iphone%2Caps%2C306&ref=nb_sb_noss_1"
data = {"Title": [], "Price": []}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
}

r = requests.get(url, headers = headers)

soup = BeautifulSoup(r.text, "html.parser")
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans:
    print(span.string)
    data["Title"].append(span.string)

for price in prices:
    if not("a-text-price" in price.get("class")):
        print(price.find("span").get_text())
        data["Price"].append(price.find("span").get_text())
        if len(data["Price"]) == len(data["Title"]):
            break

print("Number of Titles:", len(data["Title"]))
print("Number of Prices:", len(data["Price"]))


df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)
df.to_excel("data.xlsx", index=False)
