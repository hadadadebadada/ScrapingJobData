import scrapy
from scrapy import item
from scrapy.loader import ItemLoader
from funscraper.items import SimpleItem
class RaribleapiSpider(scrapy.Spider):
    name = 'RaribleApi'
    allowed_domains = ['rarible.com']
    start_urls = ['https://rarible.com/token/0x60f80121c31a0d46b5279700f9df786054aa5ee5:12937']



    def parse_item(self, response):
        print(response.body)
        #json_res = json.loads(response.body)
        return  print(response.body)
        # if not isinstance(json_res, list) or len(json_res) < 1:
        #     return None
        #
        # data = json_res[0]
        # loader = ItemLoader(item=SimpleItem())
        # loader.add_value('title', data['title']['rendered'])
        # loader.add_value('publish_date', data['date_gmt'])
        # return loader.load_item()