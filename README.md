<div align="center">
  <h3 align="center">PlayScrape</h3>
  <p align="center">
    Scrape and Visualize Playstore App Reviews
  </p>
</div>

## Description
Sebuah alat sederhana untuk melakukan scraping dan memvisualisasikan menggunakan wordcloud reviews sebuah aplikasi yang ada pada playstore

## Installation
```
# Python version 3.7 or newer
$ git clone https://github.com/byte-ai/playscrape.git
$ cd playscrape
$ pip3 install -r requirements.txt
```

## Arguments
```
# Scraping
--name      : App name
--rating    : User reviews rating
--language  : Reviews language    
--country   : User review country

# Visualize (Wordcloud)
--name      : App name

# Show DataFrame
--name      : App name
--rating    : User reviews rating
--quantity  : Total data
```

## Usage
```
# To scrape data
$ python src/scraping.py --name bukalapak --rating 4 --language id --country id

# To visualize data
$ python src/word_cloud.py --name bukalapak --rating 4

# To check the data with Pandas Dataframe
$ python src/check.py --name bukalapak --rating 4 --quantity 60
```
