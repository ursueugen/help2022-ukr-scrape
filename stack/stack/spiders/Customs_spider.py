# Customs' website dynamic, requires selenium.

# import scrapy
# from stack.items import ArticleItem

# from selenium import webdriver
# from selenium.webdriver import FirefoxOptions
# from selenium.webdriver.support.ui import WebDriverWait


# def get_browser() -> webdriver.Firefox:
#     """
#     Returns a browser abstraction.
#     """
#     opts = FirefoxOptions()
#     opts.add_argument("--headless")
#     driver = webdriver.Firefox(
#         options=opts,
#         firefox_profile=None,
#         # executable_path="/data/sources/help2022-ukr-scrape/stack/geckodriver"
#     )
#     return driver


# class CustomsSpider(scrapy.Spider):
#     """
#     Spider for MD Customs: https://customs.gov.md/ro/articles?tag=news
#     """

#     name = "Customs_spider"
#     allowed_domains = ["customs.gov.md"]
#     start_urls = [
#         "https://customs.gov.md/ro/articles?tag=news",
#     ]

#     def __init__(self):
#         self.driver = get_browser()

#     def parse(self, response):

#         self.driver.navigate(response.url)

#         links = []
#         preview_article_link = WebDriverWait(
#             self.driver).until(
#                 lambda d: d.find_element_by_xpath(
#                     "//a[@class='news-preview']/@href")
#         )
#         links.append(preview_article_link)
#         news_article_links = WebDriverWait(
#             self.driver).until(
#                 lambda d: d.find_elements_by_xpath(
#                     "//a[@class='news-link']/@href")
#         )
#         links = links + news_article_links

#         # preview_article_link = response.xpath(
#         #     "//a[@class='news-preview']/@href").get()
#         # links.append(preview_article_link)
#         # news_article_links = response.xpath(
#         #     "//a[@class='news-link']/@href").getall()
#         # links = links + news_article_links

#         print(f"LINKS: {links}")

#         for link in links:
#             yield response.follow(response.urljoin(link), self.parse_article)

#     def parse_article(self, response):
#         article = ArticleItem()
#         article['url'] = response.url
#         article['title'] = response.xpath(
#             "//h1[class='jsx-140060271']/text()"
#         ).get()
#         article['date'] = response.xpath(
#             "//span[class='jsx-2146728798 date']/text()"
#         ).get()
#         article['text'] = " ".join(
#             response.xpath(
#                 "//div[class='jsx-2943259229 article-content']//text()"
#             ).getall()
#         )
#         return article
