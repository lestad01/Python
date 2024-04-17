"""import requests
from requests.exceptions import HTTPError


for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')
    else:
        print('Success!')
request = requests.get('https://api.github.com')

request.status_code

 if request.status_code == 200:
    print('Success!')
elif request.status_code == 404:
    print('Not Found')


if request:
    print('Success!')
else:
    print('An error has occurred')
""""

##import requests

##response = requests.get('https://api.github.com')
##response.headers['Content-Type']
##response.encoding = 'utf-8'
##response.json()
##response.content


import requests

"""requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get') """

# Поиск местонахождения для запросов на GitHub
response = requests.get(
    'https://api.github.com/search/repositories',
    params=[('q': 'requests+language:python')],
)

# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')
