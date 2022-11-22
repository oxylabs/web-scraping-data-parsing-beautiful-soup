import requests

response = requests.get('https://books.toscrape.com')
if response.status_code != 200:
    print('Could not fetch the page')
    exit(1)

print('Successfully fetched the page')