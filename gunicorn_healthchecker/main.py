from gunicorn_healthchecker.server import Server
from gunicorn_healthchecker.state import State

def run(args = {}):
  
  workers = args.get('workers', 0)
  healthcheck_bind = args.get('healthcheck_bind', 8001)
  healthcheck_target_name = args.get('healthcheck_target_name', 'gunicorn')
  healthcheck_target_host = args.get('healthcheck_target_host', 'localhost')
  healthcheck_target_port = args.get('healthcheck_target_port', 80)
  healthcheck_target_endpoint = args.get('healthcheck_target_endpoint', '')

  state = State()
  state.workers = workers 

  wsgi = Server('0.0.0.0', healthcheck_bind)
  wsgi.run()

if __name__ == '__main__':
  run()