import tornado.ioloop
import tornado.web
from book import Book
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler
from edithandler import EditHandler
from booksbyauthor import BooksByAuthor

books = Book()
# This is is the main handler class
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("NU Microservice v2.7.6")

#This will fork out to the specific handlers based on the request
def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addbook", AddHandler, dict(books = books)),
        (r"/v1/updatebook", EditHandler, dict(books = books)),
        (r"/v1/booksbyauthor", BooksByAuthor, dict(books = books)),
        (r"/v1/delbook", DelHandler, dict(books = books)),
        (r"/v1/getbooks", GetHandler, dict(books = books)),
        ])
#This is the deamon that listens on port 8888 for http requests
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
