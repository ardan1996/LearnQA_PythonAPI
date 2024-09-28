import json

json_text = '{"messages": [{"message": "Thisisthefirstmessage","timestamp": "2021-06-0416: 40: 53"},{"message": "Andthisisasecondmessage","timestamp": "2021-06-0416: 41: 01"}]}'
json_first_message = '{"message": "Thisisthefirstmessage","timestamp": "2021-06-0416: 40: 53"}'
json_second_message = '{"message": "Andthisisasecondmessage","timestamp": "2021-06-0416: 41: 01"}'
obj = json.loads(json_second_message)
print(obj['message'])

