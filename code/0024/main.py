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
        (r"/login/", LoginHandler),
        (r"/clear/", ClearHandler),
        (r"/fetch/", FetchHandler),
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
        self.render("index.html")

class LoginHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        coll = self.application.db.demo
        psw_obj = coll.find_one({'name': 'password'})

        try: 
            if self.get_argument("password", None) == psw_obj['value']:
                self.set_secure_cookie('sesscode',
                        psw_obj['value'],
                        expires_days=1)
                return self.write(json.dumps({'code': 200, 'msg': 'ok'}))
            else:
                return self.write(json.dumps({'code': 1, 'msg': 'not valid'}))
        except:
            return self.write(json.dumps({'code': 2, 'msg': 'error'}))

class FetchHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        coll = self.application.db.demo
        psw_obj = coll.find_one({'name': 'password'})
        sesscode = self.get_secure_cookie('sesscode')
        print('''''')
        print(sesscode)
        print('''''')
        try: 
            if sesscode == psw_obj['value']:
                return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': []}))
            else:
                return self.write(json.dumps({'code': 1, 'msg': 'not valid'}))
        except:
            return self.write(json.dumps({'code': 2, 'msg': 'error'}))


class ClearHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.application.db.drop_collection('demo')
        coll = self.application.db.demo
        '''
         set admin password
        '''
        coll.save({'name': 'password' ,'value': 'admin'})

        return self.write(json.dumps({'code': 200, 'msg': 'cleared'}))


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