import requests

response = requests.post('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
number_responses = response.history
second_response = response

print(len(number_responses))
print(second_response.url)
