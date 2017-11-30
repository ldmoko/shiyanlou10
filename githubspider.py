import scrapy


class Github(scrapy.Spider):
    name = 'github'
    start_urls = []
    
    base_url = 'https://github.com/shiyanlou?tab=repositories&page={}'
    for i in range(1, 5):
        start_urls.append(base_url.format(i))

    def parse(self, response):
        print(response.url)
        for i in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            yield {
                    'name': i.xpath('div[1]/h3/a/text()').extract()[0].strip(),
                    'update_time': i.xpath('div[3]/relative-time/@datetime').extract()[0]
                    }
                    #print(name, update_time)


