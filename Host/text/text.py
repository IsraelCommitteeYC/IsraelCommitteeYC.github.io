from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    response = requests.get(url="https://www.timesofisrael.com/").text
    soup = BeautifulSoup(response, "html.parser")
    headlines = soup.select(selector="div .headline a")
    headlines_text = []
    headlines_href = []

    for headline in headlines[:10]:
        headlines_text.append(headline.getText().strip())
        headlines_href.append(str(headline).split('"')[1])

print(headlines_text)
print(headlines_href)
