from src.server.router import routers, find_router_by_tag
from src.server.database.pydantic_models import LoginData
from src.server.advanced.resolvers import student


student_router = find_router_by_tag(routers, 'Student')


@student_router.post('/login', response_model=int|dict)
def login(login_data: LoginData) -> int | dict:
    return student.login(login_data.login, login_data.password)
