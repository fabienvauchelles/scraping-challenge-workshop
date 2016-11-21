# Scraping workshop


## Where are the challenges ?

The challenges are [here](https://scraping-challenge.herokuapp.com).

All data are from the Titanic disaster (it reminds you [Kaggle](https://www.kaggle.com/c/titanic) ?)


## How to complete the challenge ?

### Step 1: Fill prerequisite

#### Install Python 2.7

Scrapy works only with Python 2.7.

[Please install Python 2.7, and not Python 3.x!](https://www.python.org/downloads/release/python-2710)

#### Install dependencies

On Ubuntu 16:

```
sudo apt-get install python-dev python-pip libssl-dev libxml2-dev libxslt1-dev libffi-dev
```


On Windows:

Download and install [Anaconda Distribution](https://www.continuum.io/downloads) for Python **2.7**.


On Mac OS X:

```
brew install python
```


#### Install Scrapy & Scrapoxy SDK

```
sudo pip install scrapy scrapoxy
```


### Step 2: Clone the repository

```
git clone https://github.com/fabienvauchelles/scraping-challenge-workshop.git
cd scraping-challenge-workshop
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
