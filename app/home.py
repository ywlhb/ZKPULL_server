import sys

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from swagger_server import app
if len(sys.argv) == 2:
    port = sys.argv[1]
else:
    port = 5005


http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port)
IOLoop.instance().start()
