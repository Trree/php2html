import scrapy

class QuotesSpider(scrapy.Spider):
    name = "php"
    start_urls = [
        'http://php.net/manual/en/',
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1].replace('.php', '') + ".html" 
        with open(filename, 'wb') as f:
            f.write(response.body)
	    

        for next_page in response.css('dd a::attr(href)').extract():
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
