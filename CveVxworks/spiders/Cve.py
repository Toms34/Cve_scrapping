import scrapy , json 

class CveSpider(scrapy.Spider):
    name = 'Cve' #name of spider
    allowed_domains = ['cvedetails.com'] #allowed domains
    start_urls= ["https://www.cvedetails.com/vulnerability-list/vendor_id-95/product_id-15063/Windriver-Vxworks.html"] #url for cve details of vxworks 

    def __init__(self):
        self.result=[]

    def parse(self, response):
        cves = response.xpath('string(//body)').re(r"CVE-\d{4}-\d{4,7}") #get all CVEs regex CVE-dddd-(dddd ddd) <--- 4-7 digits
        temp = response.xpath('//body//*//td//div//text()').getall() # get all the text in a td
        scores =response.xpath('//div[@class="cvssbox"]/text()').re(r"\d\.\d") #get all scores in div class cvssbox
        scores = [i if i != "0.0" else "10.0" for i in scores] # replace 0.0 with 10.0
        for i in range(len(cves)-2): # 0 to scores length-1
            self.result.append({"cve": cves[i], 
             "url": "https://www.cve.org/CVERecord?id="+cves[i], #url to cve
             "score" : scores[i] #score of cve
            })
            print(self.result[i], end="\n\n") #print result)
        json.dump(self.result, open("result.json", "w")) #save result to json file

