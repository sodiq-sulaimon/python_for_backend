import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hey there! This is a python command executed from the backend :)")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/home", basicRequestHandler)
    ])

    port = 5500
    app.listen(port)
    print(f"Server is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
