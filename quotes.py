import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["https://mathshistory.st-andrews.ac.uk/Biographies/Atiyah/quotations/"]
    start_urls = ["https://mathshistory.st-andrews.ac.uk/Biographies/Atiyah/quotations/"]

    def parse(self, response):
        pass
