import threading
from json import dumps
from gunicorn_healthchecker.state import State
from wsgiref.simple_server import WSGIServer, WSGIRequestHandler

class Server():

  def __init__(self, host: str, port: int) -> None:
    self.wsgi = WSGIServer((host, port), WSGIRequestHandler)
    self.wsgi.set_app(self.app)
    self.thread = threading.Thread(target=self.wsgi.serve_forever)

  def app(self, environ, start_response):
    state = State()
    if state.healthy:
      start_response('200 OK', [('Content-type', 'application/json; charset=utf-8')])
      return [bytes(dumps(state.dict()), 'utf-8')]
    else:
      start_response('503 Service Unavailable', [('Content-type', 'application/json; charset=utf-8')])
      return [bytes(dumps(state.dict()), 'utf-8')]

  def run(self):
    self.thread.start()

  def stop(self):
    self.wsgi.shutdown()
    self.wsgi.server_close()
    self.thread.join(1)