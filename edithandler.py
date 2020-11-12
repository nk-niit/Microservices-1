import tornado.web
import book
import json


class EditHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books

    def get(self):
        title = self.get_argument('title')
        new_title = self.get_argument('new_title')
        new_author = self.get_argument('new_author')
        result = self.books.update_book(title, new_title, new_author)
        
        if result == True:
            self.write("Updated successfully!")
        else:
            self.write("Book not found.")
        
