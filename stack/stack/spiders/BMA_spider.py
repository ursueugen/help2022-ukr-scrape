from typing import List
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

    COMMUNICATES_XPATH = "/html/body/div[2]/section/div[1]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div"
    ARTICLE_FULLTEXT_XPATH = "/html/body/div[2]/section/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/article/div[2]"

    # rules = (
    #     scrapy.spiders.Rule(
    #         scrapy.linkextractors.LinkExtractor(),
    #         callback = 'parse'
    #     ),
    # )

    def parse(self, response: scrapy.http.Response):
        # communicates = scrapy.Selector(response).xpath(BMASpider.COMMUNICATES_XPATH).getall()
        communicates = response.xpath(BMASpider.COMMUNICATES_XPATH)
        for communicate in communicates:
            article = ArticleItem()
            article['title'] = communicate.xpath('h4//a/text()').get()
            # article['text_view'] = communicate.xpath('div[3]/div/text()').get()
            article['url'] = response.urljoin(communicate.xpath('h4//a/@href').get())
            article['date'] = communicate.xpath('div[1]/div/text()').get().split(" | ")[0]
            yield response.follow(article['url'], self.parse_article, cb_kwargs=dict(article=article))

    def parse_article(self, response: scrapy.http.Response, article: ArticleItem):
        text_pieces: List[str] = (
            response.xpath("//div[@class='panel-pane pane-node-content pressreleases']")
            .xpath(
                "//*//text()[parent::p or parent::h1 or parent::h2 "
                "or parent::h3 or parent::h4 or parent::h5 or parent::h6]"
            ).getall()
        )
        article['text'] = ". ".join(text_pieces[3:-5])
        return article