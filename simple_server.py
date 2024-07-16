import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hey there! Welcome to my course selection for MSCS at Georgia Tech :)")

class courseRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        number = self.get_argument("num")
        if (number.isdigit()):
            result = "odd" if int(number) % 2 else "even"
            self.write(f"{number} is {result}")
        else:
            self.write("Invalid input")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/courses", courseRequestHandler),
        (r"/isEven", queryParamRequestHandler),

    ])

    port = 5500
    app.listen(port)
    print(f"Server is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
