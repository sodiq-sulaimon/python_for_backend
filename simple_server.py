import tornado.web
import tornado.ioloop
import json

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

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseID):
        self.write(f"Hi {studentName}, welcome to course {courseID}")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        file = open("list.txt", 'r')
        fruits = file.read().splitlines()
        file.close

        self.write(json.dumps(fruits))

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/courses", courseRequestHandler),
        (r"/isEven", queryParamRequestHandler),
        (r"/students/([A-z]+)/([0-9]+)", resourceParamRequestHandler),
        (r"/fruits", listRequestHandler)
    ])

    port = 5500
    app.listen(port)
    print(f"Server is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
