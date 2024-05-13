import scrapy
import time
from ..items import AoneplusItem

class AoneplusScrapeSpider(scrapy.Spider):
    name = "aoneplus_scrape"
    allowed_domains = ["aoneplus.com"]
    start_urls = ["https://aoneplus.com/product-category/computers-laptops/laptops/"]

    def parse(self, response):
        time.sleep(3)
        products = response.css('div.product-outer')  
        for product_url in products :
            x = []
            x = product_url.css('div.product-body a::attr(href)').getall()
            for i in x :
               # extract content inside the individual product 
               yield response.follow(i, callback=self.parse_product)


        
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    def parse_product(self, response):
        dict = AoneplusItem()
        name=response.css('h1.entry-title::text').get()
        price=response.css('bdi::text').get()
        specification=response.xpath('//div[@id="tab-description"]//ul/li/text()').getall()
        try :
             sku=response.css('span.sku::text').get()
        except:
            pass
        try:
            categories=response.css('span.posted_in > a::text').getall()
        except:
            pass
        try:
            tag = response.css('span.tagged_as a::text').get()
        except:
            pass

        if specification :
            for m in specification :
                if m == '\n' :
                    specification = []


        dict["name"]= str("".join(name)),
        dict["price"] =str("".join(price)),
        if len(specification) != 0 : 
            dict["specification"]=str(" ".join(specification)),
        dict["categories"]= str("".join(categories)),
        dict["tag"] = str("".join(tag)),
        dict["sku"] =str(sku)

        # some of the values are extract in the form of tuples so convert in string for storing in database
        dict['name'] = str(dict['name'])
        dict['price'] = str(dict['price'])
        dict['sku'] = str(dict['sku'])
        dict['categories'] = [str(cat) for cat in dict['categories']]
        dict['tag'] = str(dict['tag'])

        yield dict
        


