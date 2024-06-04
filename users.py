import json
import requests
from utilities.configurations import *
from utilities.resources import *
from payloads import *

url = get_config()['API']['baseuri'] + ApiResorces.api_users
print(url)

response_add_users = requests.post(url, json=
                                  get_payloads_users())

add_users_dict = json.loads(response_add_users.text)
print(add_users_dict['job'])
print(response_add_users)


'''
dict_response = json.loads(response.text)
print(dict_response)
'''