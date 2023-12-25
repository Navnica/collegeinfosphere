from src.server.database.models import Student


def login(login_str, password):
    student = Student.get_or_none(
        Student.phone == login_str,
        Student.password == password
    )

    return {'error': 'Incorrect login or password'} if student is None else student.id