import requests


def test_is_cookie_present():
    url = "https://playground.learnqa.ru/api/homework_cookie"
    expected_cookie = {'HomeWork': 'hw_value'}
    response = requests.get(url)
    received_cookie = response.cookies.get_dict()
    assert received_cookie == expected_cookie, f"Cookies doesnt match, recieved cookie: {received_cookie}" \
                                               f", expected: {expected_cookie} "
