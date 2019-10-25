import logging

import tornado.httpserver
import tornado.ioloop
import tornado.web
from utils.utils_options import options, define

# Define command parameter
define("port", default=None, help="Run server on a specific port, mast input", type=int)


class MainHandler(tornado.web.RequestHandler):
    """docstring for MainHandler"""

    def data_received(self, chunk):
        pass

    def get(self):
        self.write("-- This is PythonDockerDemo Master!")


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            debug=True,
        )

        handlers = [
            (r"/", MainHandler)
        ]
        super(Application, self).__init__(handlers, **settings)


def main():
    # ################parse command#######################
    options.parse_command_line()

    if options.port is None:
        options.print_help()
        return

    logging.info("Test info:Master start!")
    logging.error("Test error:Master start!")
    logging.debug("Test debug:Master start!")

    # ###########setting tornado server#####################
    global http_server

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)

    # ###########start tornado server#######################
    tornado.ioloop.IOLoop.instance().start()
    logging.info('Exit Master')


if __name__ == "__main__":
    main()
