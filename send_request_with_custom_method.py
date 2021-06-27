import requests
import RequestMethods

methods = RequestMethods.Methods
responses = [requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                           data={"method": {methods.POST.value}}),
             requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",
                           params={"method": {methods.GET.value}}),
             requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type",
                           data={"method": {methods.PUT.value}}),
             requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type",
                           data={"method": {methods.DELETE.value}})]

for response in responses:
    print(response.status_code)
    print(response.reason)
    print(response.text)
