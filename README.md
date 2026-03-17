# cobweb
A simple web crawler + indexer for Information Retrieval

cobweb is a lightweight web crawling and indexing tool built with Scrapy. It collects web pages and ranks them using a combination of TF-IDF and cosine similarity to return the most relevant results for a query.

---

## Features
- Web crawling using Scrapy
- Automatic indexing of crawled pages
- TF-IDF vectorization for document representation
- Page Rank for most relevant pages
- Cosine similarity for ranking results
- Minimal search engine (returns top 5 relevant pages)
---

## Configs

Allowed URLs:
Modify the allowed domains in `spider_crawler.py` to control which websites are crawled.

Crawler Settings:
You can tweak parameters in `settings.py` such as concurrency and request delays.

TDIDF Matrix:
`tdidf_index.py` uses alpha and beta values (thresholds) as a combination of pagerank+tfidf to yield most accurate results these can be modified


NOTE:
Setting very high concurrency may lead to crashes or timeouts depending on your system and network.

---

## Usage

1. Run the crawler

This will crawl pages and store the output in a JSON file:

scrapy crawl crawler -O index.json

---

2. Build the TF-IDF index

python pagerank.py<br>
python tfidf_index.py

This step processes the crawled data and creates a searchable index.

---

3. Search (Minimal Implementation)

- Returns the top 5 most relevant pages

