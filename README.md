# Web Scraping and Data Parsing Using Beautiful Soup

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

[<img src="https://img.shields.io/static/v1?label=&message=python&color=brightgreen" />](https://github.com/topics/python)
[<img src="https://img.shields.io/static/v1?label=&message=beautifulsoup&color=yellow" />](https://github.com/topics/beautifulsoup)
[<img src="https://img.shields.io/static/v1?label=&message=Web%20Scraping&color=important" />](https://github.com/topics/web-scraping)

This project provides a clear and concise example of how to fetch content from a website using the [Requests](https://pypi.org/project/requests/) module and then parse it using [BeautifulSoup](https://pypi.org/project/beautifulsoup4/).

## Setting Up

To run this example you will need Python 3. We recommend [setting up a virtual environment](https://docs.python.org/3/library/venv.html)

Install dependencies by running
```bash
$ pip install requests
$ pip install BeautifulSoup4
$ pip install pandas
```

**Note**: You can also install them by using the [requirements.txt](src/requirements.txt) file included in this repository.

```bash
$ pip install -r src/requirements.txt
```

## Web Scraping

A mock bookstore website called https://books.toscrape.com is our scraping target.

Use the `requests` module to fetch a page from it

```python
response = requests.get('https://books.toscrape.com')
```

Once the response is retrieved, check whether the request was successful or not by verifying the `status_code` property

```python
if response.status_code != 200:
    print('Page not found')
    exit(1)

print('Successfully fetched the page')
```

Save the script as `src/scrape.py` and run it. 

```bash
$ python3 src/scrape.py

Successfully fetched the page
```

The `requests` module has successfully retrieved the html content from the website and now all that's left is to parse it.

A working example can be found [here](src/scrape.py)

## Parse HTML

Take a look at the structure of the HTML that you're trying to scrape.

```html
<article class="product_pod">
    ...
    <h3>
        <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
    </h3>
    ...
</article>
```

The book info is neatly wrapped in an `article` tag. Inside the article, there's a heading (`h3`) that contains an anchor (`a`), which contains the title of the book inside an attribute.

```html
<a ... title="A Light in the Attic">...</a>
```

To parse this HTML content use the BeautifulSoup4 library.

Firstly, import BeautifulSoup
```python
from bs4 import BeautifulSoup
```

Then, create an instance of the `BeautifulSoup` class and load the HTML content that has been retrieved from the web page previously.

```python
soup = BeautifulSoup(response.content, 'html.parser')
```

Retrieve all the article tags

```python
articles = soup.find_all('article')
```

Define a `titles` array that will hold all the book titles extracted from the current HTML

```python
titles = []
```

Iterate through every article to extract the title attribute of the anchor tag. You may want to print the title as well, just to see whether the script works as expected

```python
for article in articles:
    title = article.h3.a.attrs['title']
    titles.append(title)
    print(title)
```

Save the script as `src/parse.py` and run it

```python
$ python3 src/parse.py                                              
Successfully fetched the page         
A Light in the Attic       
Tipping the Velvet
Soumission
...
```

All the book titles have been parsed successfully!

A working example can be found [here](src/parse.py)

## Save to csv

Printing everything to standard output can become messy at times. Instead, it is a good idea to save the results into a CSV file. 

Start by deleting the `print` function.
```python
print(title) # delete this!
```

Next, create a data frame object by using the `pandas` library. In the constructor, pass a dictionary that contains the name of the column ("Title") and an array of titles that was parsed previously.

```python
data_frame = pandas.DataFrame({'Title': titles})
```

Finally, save the data frame to a file by using the `to_csv` method

```python
data_frame.to_csv('books.csv', index=False, encoding='utf-8')
```

Save the script as `src/save.py` and execute it.

```bash
$ cd src
$ python3 save.py
Successfully fetched the page
```

Use the `cat` Unix utility to print the csv file. 

```bash
$ cat books.csv
Title
A Light in the Attic       
Tipping the Velvet
Soumission
...
```

The newly created file now contains all the book titles from the web page.

The final version of the script can be found [here](src/save.py)
