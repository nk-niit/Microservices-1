import json
import unittest
from book import Book
#from delhander import DelHandler
from gethandler import GetHandler

books = Book()

class GetBooksTest(unittest.TestCase):
    def test_get(self):
        result = books.get_books_by_author("Author4")
        print(result)
        assert result != "No books"
