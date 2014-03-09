from distutils.core import setup

setup(name='python-nmcli',
      version='0.1.0',
      description='Python wrapper around nmcli',
      author='Zach Goldberg',
      author_email='zach@zachgoldberg.com',
      url='https://github.com/ZachGoldberg/python-nmcli',
      packages=[
        'nmcli',
        ],
      classifiers=['Development Status :: 3 - Alpha'],
      long_description="""
Just a simple wrapper around nmcli.

>>> import nmcli
>>> dir(nmcli)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'con', 'dev', 'nm', 'nmcli', 'shell']
>>> nmcli.nm.status()
[{'WIFI': 'enabled', 'STATE': 'connected', 'WWAN': 'enabled', 'WWAN-HARDWARE': 'enabled', 'RUNNING': 'running', 'WIFI-HARDWARE': 'enabled'}]



"""
     )
