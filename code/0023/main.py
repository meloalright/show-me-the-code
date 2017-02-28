# -*- coding: utf-8 -*-

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import json
import pymongo
#这里是导入MongoDB

define("port", default=8002, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
        (r"/", MainHandler),
        (r"/fetch/", FetchHandler),
        (r"/submit/", SubmitHandler),
        (r"/clear/", ClearHandler),
        ]

        settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
        )

        conn = pymongo.MongoClient("localhost", 27017)
        self.db = conn["demo"]
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class FetchHandler(tornado.web.RequestHandler):
    def get(self):
        coll = self.application.db.demo
        arr = [{'name': i['name'], 'comment': i['comment']} for i in coll.find()]
        print(arr)
        return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': arr}))

class SubmitHandler(tornado.web.RequestHandler):
    def post(self):
        coll = self.application.db.demo
        obj = {
            'name': self.get_argument("name", None),
            'comment': self.get_argument("comment", None)
        }
        coll.save(obj)
        return self.write(json.dumps({'code': 200, 'msg': 'ok'}))

class ClearHandler(tornado.web.RequestHandler):
    def post(self):
        self.application.db.drop_collection('demo') 
        return self.write(json.dumps({'code': 200, 'msg': 'cleared'}))

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
