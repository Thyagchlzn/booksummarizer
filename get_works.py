from booksummarizer.pipeline.prediction import ModelEvaluationTrainingPipeline
from booksummarizer.logging import logger
from builtins import zip, str, range
import pdb, os, csv, re, io
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
from tqdm import tqdm
from shutil import rmtree
from nltk.tokenize import word_tokenize, sent_tokenize

# PARAMS
MAIN_SITE = 'https://web.archive.org/web/20210312193150/https://www.cliffsnotes.com/'

def scrape_index_pages(seed_page):
# For each summary info
    scraped_links = []

    soup = BeautifulSoup(urllib.request.urlopen(seed_page), "html.parser")
    items = soup.findAll("li", {"class": "note"})
    print("Found %d items." % len(items))

    # Go over each section
    for index, item in enumerate(items):
        # Parse section to get bullet point text
        item_title = item.find("div", {"class": "note-name"}).text
        item_url = item.find("a").get("href")

        scraped_data.append({
            "title": item_title.strip().replace(",",""),
            "url": urllib.parse.urljoin(MAIN_SITE, item_url.strip())
        })
    return scraped_data

# generate literature links
scraped_data = scrape_index_pages( 'https://web.archive.org/web/20210312193150/https://www.cliffsnotes.com/literature='+book+'?filter=ShowAll&sort=TITLE'
)
