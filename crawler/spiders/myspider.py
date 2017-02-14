from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from crawler.items import crawlerlistItem

class MySpider(BaseSpider):
    name = "epoca"
    allowed_domains = ["epocacosmeticos.com.br"]
    start_urls = ["http://www.epocacosmeticos.com.br/maquiagem"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//span[@class='pl']")
        items = []
        for titles in titles:
            item = crawlerlistItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items