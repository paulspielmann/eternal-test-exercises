from random import randint
from http.server import HTTPServer, SimpleHTTPRequestHandler

TEST_PORT = randint(30000, 32000)

# Ce code démarre un serveur web pour tester l'application sans souci
httpd = None
thread = None
def start_webserver(): #pragma: no cover
  global httpd
  global thread
  if httpd is not None:
    return thread
  import threading
  httpd = HTTPServer(('localhost', TEST_PORT), SimpleHTTPRequestHandler)
  thread = threading.Thread(target=httpd.serve_forever)
  thread.start()
  return thread

def teardown_webserver(): #pragma: no cover
  global thread
  global httpd
  if httpd is None or thread is None:
    return
  httpd.shutdown()
  thread.join()
  thread = None
  httpd = None

