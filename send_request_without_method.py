import requests

responses = [requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type"),
             requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type"),
             requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type"),
             requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")]

for response in responses:
    print(response.status_code)
    print(response.reason)
    print(response.text)
