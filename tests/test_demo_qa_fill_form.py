from data.users import student

from src.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_fill_form():
    registration_page.open_page()
    registration_page.fill_form(student)
    registration_page.assert_registered(student)
