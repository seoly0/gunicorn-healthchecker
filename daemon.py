from daemonize import Daemonize
from gunicorn_healthchecker.main import run

pid = "/tmp/gunicorn-healthchecker.pid"
daemon = Daemonize(app="gunicorn-healthchecker", pid=pid, action=run)
daemon.start()