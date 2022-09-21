import scrapy , json, re
from pydispatch import dispatcher
from scrapy import signals


class CveallSpider(scrapy.Spider): # do all cves related
    name = 'CveAll'
    allowed_domains = ['cve.mitre.org', 'nvd.nist.gov']
    cves = []
    scores = []
    final = []
    start_urls = ['https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=VxWorks']

    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def parse(self, response):
        self.cves= response.xpath('string(//body)').re(r"CVE-\d{4}-\d{4,7}") #get all CVEs regex CVE-dddd-(dddd ddd) <--- 4-7 digits
        print(self.cves)
        self.cves = list(set(self.cves)) #remove duplicates
        for index, cve in enumerate(self.cves):
            print()
            yield scrapy.Request(
            url="https://www.cvedetails.com/cve-details.php?cve_id="+str(cve),
            callback=self.second_parse,
            meta={"cve": cve, "index": index},
            dont_filter=True,
            )
        print(self.cves,self.scores)
        

    def second_parse(self, response):
        temp = response.xpath('//body//*//td//div//text()').getall()  # get all the text in a td 
        for item in temp :
            if re.findall("^\d*\.?\d+$",item)!=[]:
                temp = item
                break
        self.scores.append(temp)
        self.final.append({"cve": response.meta["cve"],
        "url": "https://www.cve.org/CVERecord?id="+response.meta["cve"], #url to cve
        "score" : temp #score of cve
        })
        print(response.meta["cve"],temp)
    
    def spider_closed(self, spider):
        print("Spider closed")
        self.scores = [i if i != "0.0" else "10.0" for i in self.scores]
        json.dump(self.final, open("resultAll.json", "w")) #save result to json file
