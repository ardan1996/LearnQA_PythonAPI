import requests

class TestCookie:
    def test_request_cookie(self):
        url = 'https://playground.learnqa.ru/api/homework_header'

        response = requests.get(url)

        header_value = dict(response.headers)

        print(header_value)

        header = (
            "Date",
            "Content-Type",
            "Content-Length",
            "Connection",
            "Keep-Alive",
            "Server",
            "x-secret-homework-header",
            "Cache-Control",
            "Expires"
        )
        assert tuple(header_value.keys()) == header, "Неверный ответ"
