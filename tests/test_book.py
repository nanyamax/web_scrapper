import unittest
from scrapy.http import HtmlResponse, Request
from books.spiders.book import BookSpider
from books.items import BooksItem

class BookSpiderTest(unittest.TestCase):
  
  def setUp(self):
    self.spider= BookSpider()
    self.example_html = """
    <html>
    <body>
    <article class="product_pod">
      <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
      <div class="product_price">
        <p class="price_color">£51.77</p>
       </div>

    </article>
    <article class="product_pod">
    
        <h3><a href="catalogue/tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a></h3>
        
           <div class="product_price">

        <p class="price_color">£53.74</p>
            </div>
        
    </article>
    <li class="next"><a href="catalogue/page-2.html">next</a></li>
    </body>
    </html>
    """
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
    book_items = [item for item  in results if isinstance(item, BooksItem)]
    pagination_requests = [
      item for item in results if isinstance(item, Request)]

    self.assertEqual(len(book_items),2)
    self.assertEqual(len(pagination_requests),1)


  def test_parse_scrapes_correct_book_information(self):
    """ Test if the spider scrapes the correct information for each book."""
    results = list(self.spider.parse(self.response))
    book_items = [item for item in results if isinstance(item, BooksItem)]
    expected_books_info = [
      {'price': '£51.77',
      'title': 'A Light in the Attic',
      'url': 'catalogue/a-light-in-the-attic_1000/index.html'}, {'price': '£53.74',
       'title': 'Tipping the Velvet',
       'url': 'catalogue/tipping-the-velvet_999/index.html'}
    ]
    self.assertEqual(len(book_items), len(expected_books_info))
    for scraped_item, expected_item in zip(book_items, expected_books_info):
      self.assertEqual((scraped_item)['title'], expected_item['title'])
      self.assertEqual((scraped_item)['price'], expected_item['price'])
      self.assertEqual((scraped_item)['url'], expected_item['url'])


  def test_parse_creates_pagination_request(self):
    """Test if the spider creates a pagination request correctly."""
    results = list(self.spider.parse(self.response))
    pagination_requests = [
      item for item in results if isinstance(item, Request)]
    
    self.assertEqual(len(pagination_requests), 1)
    #results = list(self.spider.parse(self.response))
        #next_page_request = results[-1]
        # self.assertIsInstance(next_page_request, Request)
        # self.assertEqual(
        #     next_page_request.url,
        #     "https://books.toscrape.com/catalogue/page-2.html",
        # )

  if __name__ == "__main__":
    unittest.main()