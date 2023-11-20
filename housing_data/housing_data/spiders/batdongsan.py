import scrapy
# import random

class BatdongsanSpider(scrapy.Spider):
    name = "batdongsan"
    # allowed_domains = ["batdongsan.com.vn"]
    start_urls = ["https://homedy.com/search?typeId=1&keyword=hanoi"]

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url = url, callback = self.parse, headers = self.HEADERS)

        # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    def parse(self, response):
        
        houses = response.css("div.color-orange ").get()
        # houses = response.css('div.info')
        print(houses)
        # for house in houses:
        #     print(house.css('text').get())
        #     yield{
        #         'name': house.css('text').get(),
        #     }
        # for house in houses:
            # title = house.css("a.title").get()
            # print(title)
        
