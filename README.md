# Scraping workshop


## Where are the challenges ?

The challenges are [here](https://scraping-challenge.herokuapp.com).

All data are from the Titanic disaster (it reminds you [Kaggle](https://www.kaggle.com/c/titanic) ?)

Challenges are :

1. Extract all persons from one page
2. Extract all persons from multiple pages (use pagination)
3. Bypass the user-agent


## How to complete the challenge ?

### Step 0: Fill prerequisite

Scrapy works only with Python 2.7.

[Please install Python 2.7, and not Python 3.x!](https://www.python.org/downloads/release/python-2710)


### Step 1: Clone the repository

```
git clone https://github.com/fabienvauchelles/scraping-challenge-workshop.git
cd scraping-challenge-workshop
```


### Step 2: Install all Python dependencies

```
pip install -r requirements.txt
```


### Step 3: Edit your scraper to complete the challenge

Scraper code is inside the file ```myscraper/spiders/myscraper.py```.

Items are inside the file ```myscraper/items.py```.


### Step 4: Start the scraper

```
cd scraping-challenge-workshop
scrapy crawl myscraper -t jsonlines -o persons.json
```

Exports items are inside the file ```persons.json```.


## Licence

See the [Licence](LICENCE.txt).

