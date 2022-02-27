#!/bin/bash

# scrapy crawl BMA_spider -o test_scraping/BMA_items.json -t json
# scrapy crawl Customs_spider -o test_scraping/Customs_items.json -t json
scrapy crawl Borderpolice_spider -o test_scraping/Borderpolice_items.json -t json