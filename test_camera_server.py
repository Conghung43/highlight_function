from http.server import BaseHTTPRequestHandler, HTTPServer
import logging.handlers
from datetime import datetime
LOG_FILENAME = r'log/logging.out'
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1024000, backupCount=100)
my_logger.addHandler(handler)

class MyServer(BaseHTTPRequestHandler, object):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        return
    def do_POST(self):
        global saved_image
        my_logger.info(str(datetime.now()) + ' DEBUG Receive signal from ZED ')
        self.send_response(200)
        self.end_headers()
        # time.sleep(0.2)
        saved_image = True
        print ("Sent response")
        return
if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), MyServer)
    print ('Starting server, use <Ctrl-C> to stop')
    # Thread(target= main, args=()).start()
    server.serve_forever()