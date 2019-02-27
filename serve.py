#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):

        # self.send_head()
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        for h in self.headers:
            self.wfile.write(h)
            self.wfile.write(" ")
            self.wfile.write(self.headers[h])
            self.wfile.write("\n")

httpd = SocketServer.TCPServer(("", 8080), Handler)

httpd.serve_forever()
