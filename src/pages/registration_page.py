from selene import be, have, browser, by

from data.users import Users
from path_config import TEST_FILE_PATH


class RegistrationPage:
    
    def __init__(self):
        self.first_name_input = browser.element("#firstName")
        self.last_name_input = browser.element("#lastName")
        self.email_input = browser.element("#userEmail")
        self.phone_number = browser.element("#userNumber")
        self.birth_date_input = browser.element("#dateOfBirthInput")
        self.subject_input = browser.element("#subjectsInput")
        self.upload_file_button = browser.element("#uploadPicture")
        self.current_address_input = browser.element("#currentAddress")
        self.state_list = browser.element("#state")
        self.city_list = browser.element("#city")
        self.submit_button = browser.element("#submit")
    
    @staticmethod
    def open_page():
        browser.open("/automation-practice-form")
    
    @staticmethod
    def _get_gender_input(gender):
        return browser.element(
            by.xpath(f"//input[@value='{gender}']/ancestor::div[contains(@class, 'custom-control')]"))
    
    def _set_date_from_calendar(self, day, month, year):
        self.birth_date_input.click()
        browser.element(by.xpath("//select[@class = 'react-datepicker__year-select']")).click().element(
            by.xpath(f"//option[text() = '{year}']")
        ).click()
        browser.element(by.xpath("//select[@class = 'react-datepicker__month-select']")).click().element(
            by.xpath(f"//option[text() = '{month}']")).click()
        browser.element(
            by.xpath(f"//div[contains(@class, 'react-datepicker__day') and text() = '{day}']")).click()
    
    @staticmethod
    def _set_hobbies(hobbies: tuple):
        """

        :param hobbies: Sports, Reading or Music

        """
        for hobby in hobbies:
            browser.element(by.xpath(
                f"//label[@class='custom-control-label' and text()='{hobby}']"
                "/ancestor::div[contains(@class, 'custom-checkbox')]")).should(be.clickable).click()
    
    def _set_state(self, option):
        self.state_list.click()
        browser.element(f"//div[contains(@id, 'react-select-3-option') and contains(text(), '{option}')]").click()
    
    def _set_city(self, option):
        self.city_list.click()
        browser.element(f"//div[contains(@id, 'react-select-4-option') and contains(text(), '{option}')]").click()
    
    @staticmethod
    def _assert_user_data(param, expected_value):
        (browser.element(by.xpath(f"//table/tbody//td[text() = '{param}']/following-sibling::td"))
         .should(have.text(expected_value)))
    
    def fill_form(self, user: Users):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        self.first_name_input.should(be.blank).type(user.name)
        self.last_name_input.should(be.blank).type(user.surname)
        self.email_input.should(be.blank).type(user.email)
        self._get_gender_input(user.gender).click()
        self.phone_number.type(user.number)
        self._set_date_from_calendar(user.day, user.month, user.year)
        self.subject_input.type(user.subject).press_enter()
        self._set_hobbies(user.hobby)
        self.upload_file_button.type(TEST_FILE_PATH)
        self.current_address_input.type(user.address)
        self._set_state(user.state)
        self._set_city(user.city)
        self.submit_button.click()
    
    def assert_registered(self, user: Users):
        self._assert_user_data("Student Name", f"{user.name} {user.surname}")
        self._assert_user_data("Student Email", user.email)
        self._assert_user_data("Gender", user.gender)
        self._assert_user_data("Mobile", user.number)
        self._assert_user_data("Date of Birth", f"{user.day} {user.month},{user.year}")
        self._assert_user_data("Subjects", user.subject)
        self._assert_user_data("Hobbies", f"{user.hobby[0]}, {user.hobby[1]}")
        self._assert_user_data("Picture", TEST_FILE_PATH.split("\\")[-1])
        self._assert_user_data("Address", user.address)
        self._assert_user_data("State and City", f"{user.state} {user.city}")
