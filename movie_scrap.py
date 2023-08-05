import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
url = 'https://www.imdb.com/chart/top'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())
movies=soup.find_all('h3',{'class':'ipc-title__text'})
rating=soup.find_all('span',{'class':'ipc-rating-star'})
#print(rating)
#print(movies)
i=0
with open('Movies.csv','w',newline='',encoding='utf-8') as file:
     writer=csv.writer(file)
     writer.writerow(['Movie Title ','Movie Rating'])
     for movie, rate in zip(movies, rating):
        title = movie.text
        movie_rating = rate.text
        i+=1
        if i<=251:
          print(f"{title}  - {movie_rating}")
          writer.writerow([title,movie_rating])
print("Done!")