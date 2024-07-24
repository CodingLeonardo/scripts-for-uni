import scrapy
from scrapy.http import Response
import json
from pathlib import Path

class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["elcodigoperfecto.blog"]

    def start_requests(self):
        def func(post):
            return post["url"]
        
        with open(Path('./posts.json').resolve(), "r") as data:
            posts = json.load(data)
            urls = list(map(func, posts))
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response):
        SELECTOR_POST_TITLE = "h2.entry-title a::text"
        SELECTOR_POST_CONTENT = ".entry-content"
        SELECTOR_POST_ID = '.post::attr("id")'

        title = str(response.css(SELECTOR_POST_TITLE).extract_first())
        content = str(response.css(SELECTOR_POST_CONTENT).extract_first())
        post_id = str(response.css(SELECTOR_POST_ID).extract_first())

        post_file = open(Path('./posts/' + post_id + ".text").resolve(), "w")
        post_file.write(title + "\n \n" + content)
        post_file.close()
        pass
