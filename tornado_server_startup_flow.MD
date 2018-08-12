tornado服务器启动流程


torado服务器启动步骤主要分为：
1. 初始化tornado.httpserver.HTTServer实例，该步骤读取tornado.web.Applicaiton实例，配置tornado.httpserver.HTTServer。
2. 创建socket监听，在ioloop（事件循环）注册事件和回调函数（执行tornado.httpserver.HTTServer实例方法listen()),
3. 启动事件循环


详细流程说明：
此流程会列举出启动流程中主要的tornado源码，以便更深入的其细节。该过程会大量应用asyncio模块。

1.初始化HTTPServer实例.初始化HTTPServer实例时，在执行构造方法__init__之前，会先执行方法initialize。该过程通过__new__方法实现。HTTPServer类的__new__方法继承util.Configurable()类
	流程代码：
	http_server = tornado.httpserver.HTTPServer(app)

启动tornado过程代码
最原始回调函数：tornado.tcpserve.TCPServer()_handle_connection(self, connection, address)


过程代码
	http_server.listen(options.port, options.ip)
	 	tornado.tcpserve.TCPServer().self.add_sockets(sockets)
	 		self._handlers[sock.fileno()] = add_accept_handler( sock, self._handle_connection)

	 	tornado.netutil.def add_accept_handler(sock, callback)
	 		def accept_handler(fd, events):
	 			callback(connection, address)
	 		def remove_handler()
	 		io_loop.add_handler(sock, accept_handler, IOLoop.READ)
	 			tornado.platform.asyncio.py.BaseAsyncIOLoop(IOLoop).add_handler(self, fd, handler, events)
	 				self.asyncio_loop.add_reader(fd, self._handle_events, fd, IOLoop.READ)
	 				self.asyncio_loop.add_writer(fd, self._handle_events, fd, IOLoop.WRITE)
	 					asyncio.selector_events.py.BaseSelectorEventLoop(base_events.BaseEventLoop).add_writer(self, fd, callback, *args)


	tornado.ioloop.IOLoop.current().start()
		tornado.platform.asyncio.py.BaseAsyncIOLoop(IOLoop).start(self)
		self.asyncio_loop.run_forever()





