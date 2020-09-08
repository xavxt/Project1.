import scrapy
import requests


url = 'http://www.ite.edu.sg'

r = requests.get(url)

print("Status code:")
print("\t *", r.status_code)
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")


class NewSpider (scrapy.Spider):
    file = open("./save.json", mode="w+")
    name = "new_spider"
    start_urls = ['https://www.ite.edu.sg/']

    def parse(self, response):

        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

            page_selector = '.next a ::attr(href)'
            next_page = response.css(page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )


