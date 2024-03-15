from setuptools import setup, find_packages

setup(
  name='gunicorn-healthchecker',
  version='0.1.0',
  packages=find_packages(
    include=[
      'gunicorn_healthchecker'
    ]
  ),
  install_requires=[
    'psutil',
    'requests',
  ]
)