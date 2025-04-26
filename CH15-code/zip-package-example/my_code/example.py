import requests

response = requests.get('https://pypi.org')
print(response.content)
