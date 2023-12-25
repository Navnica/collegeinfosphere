from src.server.database.models import Staff


def login(login_str, password):
    staff = Staff.get_or_none(
        Staff.phone == login_str,
        Staff.password == password
    )

    return {'error': 'Incorrect login or password'} if staff is None else staff.id
