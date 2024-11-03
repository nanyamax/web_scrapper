import unittest
from scrapy.http import HtmlResponse, Request
from books.spiders.book import BookSpider
from books.items import BooksItem

class BookSpiderTest(unittest.TestCase):
  
  def setUp(self):
    self.spider= BookSpider()
    self.example_html = """Insert the example HTML here"""
    self.response = HtmlResponse(
      url = "https://books.toscrape.com",
      body=self.example_html,
      encoding="utf_8"
    )

  def test_parse_scrapes_all_items(self):
    """ Test if the spider scrapes books and pagination links."""
    #collect the items produced by the generator in a list
    #so that it's possible to iterate over it more than once.
    results = list(self.spider.parse(self.response))
    
    #There should be two book items and one pagination request
    book_items = []
    pagination_requests = []
    self.assertEqual(len(book_items),2)
    self.assertEqual(len(pagination_requests),1)


  def test_parse_scrapes_correct_book_information(self):
    """ Test if the spider scrapes the correct information for each book."""
    pass


  def test_parse_creates_pagination_request(self):
    """Test if the spider creates a pagination request correctly."""
    pass

  if __name__ == "__main__":
    unittest.main()