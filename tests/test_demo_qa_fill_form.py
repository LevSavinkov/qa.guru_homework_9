from data.users import student

from src.pages.registration_page import RegistrationPage


registration_page = RegistrationPage()

def test_fill_form():
    registration_page.open_browser()
    registration_page.delete_banners()
    registration_page.fill_form(student)
    registration_page.submit_button.click()
    registration_page.assert_registered(student)
