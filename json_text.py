import json

json_text = '{"messages": [{"message": "Thisisthefirstmessage","timestamp": "2021-06-0416: 40: 53"},{"message": "Andthisisasecondmessage","timestamp": "2021-06-0416: 41: 01"}]}'

obj = json.loads(json_text)

print(obj['messages'][1]['message'])
