import requests

payload_get = {"method":"GET"}
payload_post = {"method":"POST"}
payload_put = {"method":"PUT"}
payload_delete = {"method":"DELETE"}
payload_head = {"method":"HEAD"}
payload_options = {"method":"OPTIONS"}
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response = requests.get(url)
print('1. ' + response.text, response.status_code)

types_requests = [requests.head, requests.options]
payload = [payload_head, payload_options]
for res, p in zip(types_requests, payload):
    response = res(url, data=p)
    print('2. ' + response.text, response.status_code)


response = requests.get(url, params=payload_get)
print('3. ' + response.text, response.status_code)

types_requests = [requests.post, requests.put, requests.delete]
payload = [payload_post, payload_put, payload_delete]
for res, p in zip(types_requests, payload):
    response = res(url, data=p)
    print('3. ' + response.text, response.status_code)

payload = [payload_get, payload_post, payload_put, payload_delete, payload_head, payload_options]
for p in payload:
    response = requests.get(url, params=p)
    print('4(GET). '+ response.text, response.status_code)

payload = [payload_get, payload_post, payload_put, payload_delete, payload_head, payload_options]
for p in payload:
    response = requests.post(url, data=p)
    print('4(POST). '+ response.text, response.status_code)

payload = [payload_get, payload_post, payload_put, payload_delete, payload_head, payload_options]
for p in payload:
    response = requests.put(url, data=p)
    print('4(PUT). '+ response.text, response.status_code)

payload = [payload_get, payload_post, payload_put, payload_delete, payload_head, payload_options]
for p in payload:
    response = requests.delete(url, data=p)
    print('4(DELETE). '+ response.text, response.status_code)

payload = [payload_get, payload_post, payload_put, payload_delete, payload_head, payload_options]
for p in payload:
    response = requests.head(url, data=p)
    print('4(HEAD). '+ response.text, response.status_code)

payload = [payload_get, payload_post, payload_put, payload_delete, payload_head, payload_options]
for p in payload:
    response = requests.options(url, data=p)
    print('4(OPTIONS). '+ response.text, response.status_code)
