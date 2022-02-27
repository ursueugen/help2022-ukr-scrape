import scrapy
from stack.items import ArticleItem


class BorderPoliceSpider(scrapy.Spider):
    """
    Spider for MD Border police: https://www.border.gov.md/noutati
    """
    
    name = "Borderpolice_spider"
    allowed_domains = ["www.border.gov.md"]
    start_urls = [
        "https://www.border.gov.md/noutati",
    ]
    
    def parse(self, response):
        
        urls = response.xpath(
            "//div[@class='view-content row']//article//a/@href"
        ).getall()

        # for url in urls:

    
    def parse_article(self, response, article: ArticleItem):
        raise NotImplementedError