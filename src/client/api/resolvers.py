import requests
from requests import Response
import json
import settings

server_url: str = f'http://{settings.SERVER_HOST}:{settings.SERVER_PORT}'


def server_available(func):
    def need_it(*args, **kwargs):
        try:
            requests.get(url=server_url)
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            return {'error': 'Server not available'}

    return need_it


@server_available
def student_login(login_str, password):
    data = {'login': login_str, 'password': password}

    answer = requests.post(
        url=f'{server_url}/student/login', data=json.dumps(data)
    )

    return answer.json()


@server_available
def staff_login(login_str, password):
    data = {'login': login_str, 'password': password}

    answer = requests.post(
        url=f'{server_url}/staff/login', data=json.dumps(data)
    )

    return answer.json()
