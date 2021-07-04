import requests


def test_is_header_present():
    url = "https://playground.learnqa.ru/api/homework_header"
    expected_headers = {'Date': 'Sun, 04 Jul 2021 12:28:22 GMT', 'Content-Type': 'application/json',
                        'Content-Length': '15', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10',
                        'Server': 'Apache', 'x-secret-homework-header': 'Some secret value',
                        'Cache-Control': 'max-age=0', 'Expires': 'Sun, 04 Jul 2021 12:28:22 GMT'}

    response = requests.get(url)
    received_headers = dict(response.headers)
    assert received_headers.keys() == expected_headers.keys(), "headers mismatched"

    # remove time-depending fields from both expected and received headers
    expected_headers.__delitem__('Date')
    expected_headers.__delitem__('Expires')
    received_headers.__delitem__('Date')
    received_headers.__delitem__('Expires')
    assert received_headers == expected_headers, "headers content mismatched"




