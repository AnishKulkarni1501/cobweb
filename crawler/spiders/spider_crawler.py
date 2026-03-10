import scrapy
from urllib.parse import urljoin, urlparse
import re


class WebCrawler(scrapy.Spider):

    name = "crawler"

    allowed_domains = ["en.wikipedia.org"]

    start_urls = [
        "https://en.wikipedia.org/wiki/Computer_science"
    ]

    banned_extensions = (
        ".jpg",".jpeg",".png",".gif",".svg",
        ".pdf",".zip",".rar",".mp4",".mp3"
    )

    def parse(self, response):

        content_type = response.headers.get("Content-Type", b"").decode()

        if "text/html" not in content_type:
            return

        title = response.css("title::text").get()

        text_nodes = response.xpath("//p//text()").getall()

        text = " ".join(response.css("#mw-content-text p::text").getall())
        text = re.sub(r"[^a-zA-Z ]", " ", text).lower()

        links = response.css("a::attr(href)").getall()

        absolute_links = []

        for link in links:

            url = urljoin(response.url, link)

            if not url.startswith("http"):
                continue

            if url.endswith(self.banned_extensions):
                continue

            if "/wiki/" not in url:
                continue

            if ":" in urlparse(url).path:
                continue

            absolute_links.append(url)

        absolute_links = absolute_links[:50]

        yield {
            "url": response.url,
            "title": title,
            "text": text,
            "links": absolute_links
        }

        for link in absolute_links:
            yield scrapy.Request(link, callback=self.parse)
    