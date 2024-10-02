import requests
import time

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'
response = requests.get(url)

parsed_response_text = response.json()
print('token: ' + parsed_response_text["token"])

token = {"token":parsed_response_text["token"]}
second = parsed_response_text["seconds"]
get_token = requests.get(url, params=token)
response = get_token.json()
print('status: ' + response['status'])
print('waiting in seconds: ' + str(parsed_response_text["seconds"]))

time.sleep(second)

get_token = requests.get(url, params=token)
response = get_token.json()
print('result: ' + str(response['result']))
print('status: ' + response['status'])
