import scrapy


class KotvoSpider(scrapy.Spider):
    name = "kotvo"
    allowed_domains = ["www.kotsovolos.gr"]
    start_urls = ["https://www.kotsovolos.gr/household-appliances/fridges/fridge-freezers"]

    headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }

    custom_settings = {
    'DOWNLOAD_DELAY': 4
    }

    def parse(self, response):
        for page in range(1,11):
            url = f'https://www.kotsovolos.gr/api/ext/getProductsByCategory?params=pageNumber%3D{page}%26pageSize%3D36%26catalogId%3D10551%26langId%3D-24%26orderBy%3D5&catId=35822&storeId=10151&isCPage=false'
            yield scrapy.Request(url, headers=self.headers ,callback=self.parse_product)


    def parse_product(self, reponse):
        data = reponse.json()['catalogEntryView']
        for i in data:
            uniqueid = i["uniqueID"]
            name = i["name"]
            url = i["UserData"][0]['seo_url']
            price = i["price_EUR"]

            yield{'UniqueID': uniqueid,
                'Name' : name,
                'URL' : url,
                'Price' : price        
                }

