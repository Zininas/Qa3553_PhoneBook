import uuid

from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        email=f"alex_{random_suffix}@gmail.com",
        password="Password123$",
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.submit_registration()
    assert registration_page.is_registered() is True

def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        email="alexgmail.com",
        password="Password123$",
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        email="alex@gmail.com",
        password="P123$",
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_exist_user(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        email="margo@gmail.com",
        password="Mmar123456$",
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.submit_registration()

    assert registration_page.get_alert_text()=="User already exist"
    registration_page.accept_alert()
