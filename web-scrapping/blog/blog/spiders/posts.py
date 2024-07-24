import scrapy
from scrapy.http import Response

class PostsSpider(scrapy.Spider):
  name = "posts"
  allowed_domains = ["elcodigoperfecto.blog"]
  start_urls = ['https://elcodigoperfecto.blog/category/python',
                'https://elcodigoperfecto.blog/category/python/page/2/']

  def parse(self, response: Response):
    SELECTOR_POSTS = "#content > .post"
    SELECTOR_POST_TITLE = "h2.entry-title a::text"
    SELECTOR_POST_URL = 'h2.entry-title a::attr("href")'
    for post in response.css(SELECTOR_POSTS):
      yield {
        "title": post.css(SELECTOR_POST_TITLE).extract_first(),
        "url": post.css(SELECTOR_POST_URL).extract_first()
      }
    pass