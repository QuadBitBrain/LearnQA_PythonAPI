import json

string_json = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
              '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj_json = json.loads(string_json)
print(obj_json['messages'][1]['message'])
