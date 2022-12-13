import requests
import pprint
# cnnected api which you want
api = '32008174-e51212efba0878bfd3961bcd7'
query = ''
api_url = f'https://pixabay.com/api/?key={api}&q={query}'
response = requests.get(api_url)
res = response.json()
data = res.get('hits')
for url in data:
    url_list = url.get('webformatURL')
    file = open('iamge.txt', 'a+')
    file.write(url_list+'\n')
    file.close()

with open('iamge.txt', 'r') as file:
    url_data = file.readlines()
i=0
for image in url_data:
    strip = image.strip('\n')
    strip_url = requests.get(strip)
    with open(f'image/{i}.jpg', 'wb') as file:
        file.write(strip_url.content)
    i+=1