import requests
import json
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
awaitInSeconds = json.loads(response.text)['seconds'] + 1
token = json.loads(response.text)['token']

# Проверка, что джоба стартанула
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
if response.text.__contains__('"status":"Job is NOT ready"'):
    print(f"Task started")
else:
    print(f"Something went wrong: {response.text}")
    exit()

# Ожидание отрабатывания джобы и проверка удачности выполнения
print(f"waiting for: {awaitInSeconds} seconds")
time.sleep(awaitInSeconds)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
if response.text.__contains__('"result":') and response.text.__contains__('"status":"Job is ready"'):
    print(response.text)
else:
    print(f"Something went wrong: {response.text}")
