from faker import Faker

from models.user import User

fake = Faker()


def create_user(email=None, password=None):
    return User(
        email=email if email is not None else fake.unique.email(),
        password=password if password is not None else "Password123$",  # Гарантированно валидный пароль
    )


EXISTING_USER_EMAIL = "margo@gmail.com"
EXISTING_USER_PASSWORD = "Mmar123456$"
INVALID_EMAIL = "margogmail.com"
INVALID_PASSWORD = "Mmar123"


def existing_user():  # Исправлена опечатка в имени функции
    return create_user(email=EXISTING_USER_EMAIL, password=EXISTING_USER_PASSWORD)


def invalid_email_user():
    return create_user(email=INVALID_EMAIL, password=EXISTING_USER_PASSWORD)


def invalid_password_user():
    return create_user(email=EXISTING_USER_EMAIL, password=INVALID_PASSWORD)
