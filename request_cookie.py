import requests

class TestCookie:
    def test_request_cookie(self):
        url = 'https://playground.learnqa.ru/api/homework_cookie'

        response = requests.get(url)

        cookie_value = dict(response.cookies)

        print(cookie_value)

        cookie = {'HomeWork': 'hw_value'}

        assert cookie_value == cookie, "Неверный ответ"
