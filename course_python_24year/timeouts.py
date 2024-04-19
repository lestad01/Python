import requests
from requests.exceptions import Timeout

try:
    response = requests.get('https://api.github.com', timeout=60)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')


## response = requests.get('https://api.github.com', timeout=3.05)
## print(response)
