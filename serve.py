#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import datetime

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):

        # Set MIME type
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        # Banner
        self.wfile.write("MIRROR BROWSER HEADERS - ")
        d = str(datetime.datetime.now())
        self.wfile.write(d)
        self.wfile.write("\n\n")

        # Dump HTTP headers supplied by browser
        for h in self.headers:
            self.wfile.write(h)
            self.wfile.write(" ")
            self.wfile.write(self.headers[h])
            self.wfile.write("\n")

httpd = SocketServer.TCPServer(("", 8080), Handler)

httpd.serve_forever()
