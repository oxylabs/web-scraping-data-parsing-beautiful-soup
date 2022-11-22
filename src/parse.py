import requests
from bs4 import BeautifulSoup

response = requests.get('https://books.toscrape.com')
if response.status_code != 200:
    print('Could not fetch the page')
    exit(1)

print('Successfully fetched the page')

soup = BeautifulSoup(response.content, 'html.parser')
articles = soup.find_all('article')

titles = []
for article in articles:
    title = article.h3.a.attrs['title']
    titles.append(title)
    print(title)