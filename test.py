from gunicorn_healthchecker import run

run({
  'workers': 3,
  'healthcheck_target_host': 'localhost',
  'healthcheck_target_port': 8000,
})