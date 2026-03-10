# cobweb : A simple webcrawler + indexer used for Information Retrival
<p>Built using scrapy , uses TF-IDF and cosine similarity to yield most accurate results</p>

<p>Change allowed urls under spider_crawler.py to get more diverse web pages</p>
<p>You can modify the settings.py <b>BUT NOTE:</b> requesting too many concurrent pages at a time may cause a crash/timeouts</p>

### Usage

### Run crawler

```bash
scrapy crawl crawler -O index.json
```

### Build TDIDF matrix and index



```bash
python tfidf_index.py
```

Minimal search has been implemented.
