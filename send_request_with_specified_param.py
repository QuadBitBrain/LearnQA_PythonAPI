import requests
import RequestMethods

methods = RequestMethods.MethodsShort

for method in methods:
    responses = [requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                               data={"method": {method.value}}),
                 requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",
                              params={"method": {method.GET.value}}),
                 requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type",
                              data={"method": {method.PUT.value}}),
                 requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type",
                                 data={"method": {method.DELETE.value}})]

    for response in responses:
        if response.request.method != method.value and response.status_code == 200 and response.reason == "OK"\
                and response.text == '{"success":"!"}':
            print(f"Request method was: {response.request.method}, and param was: {method.value}")
