import requests

from getpass import getpass

requests.get('https://api.github.com/user', auth=('username', getpass()))
