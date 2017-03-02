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
        (r"/fetch-weather/", FetchWeatherHandler),
        (r"/submit/", SubmitHandler),
        (r"/clear/", ClearHandler),
        ]
        settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "templates/static"),
        debug=True,
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
        '''
        start
        '''
        print('starting fetch index')
        '''
        end
        '''
        print('end fetch index')
        self.render("index.html")



class FetchWeatherHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    @tornado.gen.coroutine
    def get(self):
        '''
        start
        '''
        print('starting fetch weather')
        '''
        start
        '''
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch("http://api.jirengu.com/weather.php")
        '''
         @ tornado.escape.json_decode
        '''
        data = tornado.escape.json_decode(response.body)
        weather_dict = {
            'city': data['results'][0]['currentCity'],
            'pm25': data['results'][0]['pm25']
        }
        '''
        end
        '''
        print('end fetch weather')
        '''
        end
        '''
        return self.write(weather_dict)



class FetchHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        coll = self.application.db.demo
        find = coll.find()
        arr = [{'name': i['name'], 'comment': i['comment']} for i in find]
        #翻转
        arr.reverse()
        return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': arr}))

class SubmitHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        coll = self.application.db.demo
        obj = {
            'name': self.get_argument("name", None),
            'comment': self.get_argument("comment", None)
        }
        coll.save(obj)
        return self.write(json.dumps({'code': 200, 'msg': 'ok'}))

class ClearHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.application.db.drop_collection('demo') 
        return self.write(json.dumps({'code': 200, 'msg': 'cleared'}))

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print('running')
    main()
