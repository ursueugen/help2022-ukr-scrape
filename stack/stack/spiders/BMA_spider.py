import scrapy
from stack.items import ArticleItem


class BMASpider(scrapy.Spider):
    """
    Spider for BMA - Biroul Migratie si Azil
    http://bma.gov.md/ro
    """
    name = "BMA_spider"
    allowed_domains = ["bma.gov.md"]
    start_urls = [
        "http://bma.gov.md/ro",
    ]

    COMMUNICATES_XPATH = "/html/body/div[2]/section/div[1]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div"

    def parse(self, response: scrapy.http.Response):
        communicates = scrapy.Selector(response).xpath(BMASpider.COMMUNICATES_XPATH)
        
        for communicate in communicates:
            article = ArticleItem()
            article['title'] = communicate.xpath('h4/a/text()').extract()
            article['url'] = communicate.xpath('h4/a/@href').extract()[0]
            # article['date'] = communicate.xpath('div[3]/div/text()').extract()[0]
            # article['text'] = communicate.xpath('div[3]/div/text()').extract()[0]
            yield article
            