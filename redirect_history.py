import requests

responseHistory = requests.get("https://playground.learnqa.ru/api/long_redirect").history
redirectCount = 0
for responseHistoryItem in responseHistory:
    if responseHistoryItem.is_redirect:
        redirectCount += 1

print(f"Количество редиректов: {redirectCount}")
print(f"Конечный url: {responseHistory[-1].url}")
