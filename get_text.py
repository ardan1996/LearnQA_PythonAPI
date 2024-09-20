import requests

get_text = requests.get('https://playground.learnqa.ru/api/get_text')
print(get_text.text)
