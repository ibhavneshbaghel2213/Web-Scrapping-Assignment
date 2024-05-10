import scrapy

class TestsiteSpider(scrapy.Spider):
    name = "testSite"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/static/computers/tablets"]

    def parse(self, response):
        for card in response.css('div.thumbnail'):
            yield {
                'Name': card.css('a.title::text').get(),
                'Price': card.css('h4::text').get(),
                'Review': card.css('p::attr(data-rating)').get()
            }

        numberOfPages = len(response.css('a.page-link'))
        BaseUrl = 'https://webscraper.io/test-sites/e-commerce/static/computers/tablets'
        for page in range(2, numberOfPages) :
            Siteurl = BaseUrl + f'?page={page}'
            print(Siteurl)
            yield response.follow(Siteurl, callback=self.parse)
