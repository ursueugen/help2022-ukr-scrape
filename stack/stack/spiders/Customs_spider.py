import scrapy
from stack.items import ArticleItem


class CustomsSpider(scrapy.Spider):
    """
    Spider for MD Customs: https://customs.gov.md/ro/articles?tag=news
    """

    name = "Customs_spider"
    allowed_domains = ["customs.gov.md"]
    start_urls = [
        "https://customs.gov.md/ro/articles?tag=news",
    ]

    def parse(self, response):
        raise NotImplementedError
    
    def parse_article(self, response, article: ArticleItem):
        raise NotImplementedError