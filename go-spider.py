from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from CveVxworks.spiders.Cve import CveSpider
from CveVxworks.spiders.CveAll import CveallSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(CveSpider)
process.crawl(CveallSpider)
process.start()