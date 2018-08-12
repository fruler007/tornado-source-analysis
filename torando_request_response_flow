
tornado请求响应流程
	asyncio.base_events.py.BaseEventLoop(events.AbstractEventLoop).run_forever(self)

	asyncio.selector_events.py.BaseSelectorEventLoop(base_events.BaseEventLoop)._read_from_self(self)

	tornado.platform.asyncio.py.AsyncIOMainLoop(BaseAsyncIOLoop)._handle_events(self, fd, events)
		fileobj, handler_func = self.handlers[fd]
        handler_func(fileobj, events)

    tornado.httpserver.py.HTTPServer(TCPServer, Configurable,httputil.HTTPServerConnectionDelegate)._handle_connection(self, connection, address)
    	stream = IOStream(connection,
                                  max_buffer_size=self.max_buffer_size,
                                  read_chunk_size=self.read_chunk_size)

        future = self.handle_stream(stream, address)

    Configurable,httputil.HTTPServerConnectionDelegate).handle_stream(self, stream, address)
    	context = _HTTPRequestContext(stream, address,
                                      self.protocol,
                                      self.trusted_downstream)
        conn = HTTP1ServerConnection(
            stream, self.conn_params, context)
        self._connections.add(conn)
        conn.start_serving(self)