import requests
import base64

country_link = 'https://restcountries.com/v2/all'
api_data = requests.get(country_link)
res = api_data.json()
country_name = []
for link in res:
    name = link.get('name')
    country_name.append(name)

user_name = 'yourusername'
user_pass = 'your_password'
token = base64.b64encode(f'{user_name}:{user_pass}.'.encode())
wp_access = {'Authorization': f'Basic {token.decode("utf-8")}'}
url = 'yourwebsite/wp-json/wp/v2/categories'
for catagory in country_name:
    data = {'name': catagory}
    responses = requests.post(url, data=data, headers=wp_access)
    print(responses)


