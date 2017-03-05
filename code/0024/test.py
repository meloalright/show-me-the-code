# -*- coding: utf-8 -*-

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.httpclient
import tornado.web
import tornado.gen
import datetime
from tornado.options import define, options

import json
import pymongo

define("port", default=8002, help="run on the given port", type=int)



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
        (r"/", MainHandler),
        ]
        settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "templates/static"),
        debug=True,
        cookie_secret='knomisnaowepcoii'
        )

        conn = pymongo.MongoClient("localhost", 27017)
        self.db = conn["demo"]
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        if self.get_secure_cookie('komi'):
            print(self.get_secure_cookie('sesscode'))
            return self.write({'code': 200, 'msg': 'setted..'})


        else:
            self.set_secure_cookie('komi',
                        'value',
                        expires_days=1)
            return self.write({'code': 200, 'msg': 'setting now!'})



def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    '''
    print
    '''
    print('running')
    main()