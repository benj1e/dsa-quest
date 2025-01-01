import scrapy


class LeetcodeScraperSpider(scrapy.Spider):
    name = "leetcode_scraper"
    allowed_domains = ["leetcode.com"]
    start_urls = ["https://leetcode.com"]

    def parse(self, response):
        pass
