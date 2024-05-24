import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = requests.get('https://www.imdb.com/chart/top/', headers=headers)
soup = BeautifulSoup(response.text,'lxml')
data = soup.find_all('div', class_='sc-b189961a-0 hBZnfJ cli-children')


list_of_movies = []
for i in data:
    dict = {}
    dict['name'] = i.find('a').find('h3').text
    dict['link'] = 'https://www.imdb.com/'+ i.find('a').attrs['href']
    dict['rating'] = i.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').attrs['aria-label'].replace('IMDb rating:','').strip()
    list_of_movies.append(dict)


df = pd.DataFrame(list_of_movies)
df.to_excel('IMDB.xlsx')