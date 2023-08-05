import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
url = 'https://www.imdb.com/chart/top'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())
movies=soup.find_all('h3',{'class':'ipc-title__text'})
print(movies)
for movie in movies:
        title=movie.text
        print(f"title is {title}")
        #print(title)