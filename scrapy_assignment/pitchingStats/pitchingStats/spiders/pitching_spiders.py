import scrapy

class PitchingSpider(scrapy.Spider):
    name = "pitching"
    start_urls = [
        'https://www.mlb.com/stats/pitching/innings-pitched/2019'
        ##'https://www.mlb.com/stats/pitching/innings-pitched/2019?page=2',
        ##'https://www.mlb.com/stats/pitching/innings-pitched/2019?page=3',
        ##'https://www.mlb.com/stats/pitching/innings-pitched/2019?page=4'
    ]

    def parse(self, response): 
        page = response.url.split("/")[-2]
        filename = f'pitching-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
