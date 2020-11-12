import tornado.web
import book
import json


class BooksByAuthor(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books

    def get(self):
        author = self.get_argument('author')
        result = self.books.get_books_by_author(author)
        
        self.write(result)
        
