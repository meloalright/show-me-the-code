#main.py
import os
import time
import tornado.ioloop
import tornado.web
import tornado.gen
from tornado.concurrent import Future
from tornado.httpclient import AsyncHTTPClient
from tornado.options import define, options, parse_command_line

define("debug", default=True, help="run in debug mode")



class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.render('index.html', messages=['1', '2', '3', 'response'])


k = 0
class MessageHandler(tornado.web.RequestHandler):

    def post(self):
        return self.write({'msg':['ok'], 'len': 1})
    @tornado.gen.coroutine
    def get(self):
        global k
        self.future = Future()
        k += 1
        messages = yield self.future
        if self.request.connection.stream.closed():
            return
        self.write(dict(messages=messages))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/message", MessageHandler)
        ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug,
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print('>> running: 8888')
    tornado.ioloop.IOLoop.current().start()
