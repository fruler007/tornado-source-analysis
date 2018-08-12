# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import torndb
import redis
import config
from tornado.options import options, define
from config import settings
from url_pattern import routing_maps

define(name='port', type=int, default=8000, help='server run on given port')
define(name='ip', type=str, default='127.0.0.1', help='server run on given ip')


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)


        ### 配置数据库
        self.db = torndb.Connection(**config.mysql_db)
        self.redis = redis.StrictRedis(**config.redis)


if __name__ == '__main__':
    # tornado.options.options.logging = 'warning'
    # tornado.options.options.log_file_prefix = config.log_path
    tornado.options.parse_command_line()
    app = Application(routing_maps, **settings)

    # 主要完成服务器启动前的参数配置工作
    http_server = tornado.httpserver.HTTPServer(app)

    # 主要完成socket的创建工作
    http_server.listen(options.port, options.ip)



    #tornado.ioloop.IOLoop.current()
    # 启动事件循环工作
    tornado.ioloop.IOLoop.current().start()