import unittest
from selenium import webdriver

from tests.helper_methods import create_selenium_config

from tests.constants import BASE_URL, LOGIN_URL, ERROR_URL, SEARCH_URL
from tests.constants import LOGIN_TITLE_ID, SEARCH_TITLE_ID
from tests.constants import USERNAME_INPUT_ID, PASSWORD_INPUT_ID, LOGIN_BUTTON_ID, LOGOUT_BUTTON_ID
from tests.constants import ADMIN_USERNAME, ADMIN_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD


class AuthenticationTest(unittest.TestCase):

    def setUp(self):
        self.options = create_selenium_config()
        self.driver = webdriver.Firefox(firefox_options=self.options)
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def input_username_password_and_login(self, username, password):
        self.driver.find_element_by_id(USERNAME_INPUT_ID).send_keys(username)
        self.driver.find_element_by_id(PASSWORD_INPUT_ID).send_keys(password)
        self.driver.find_element_by_id(LOGIN_BUTTON_ID).click()

    def assert_search_page_title(self):
        home_title = self.driver.find_element_by_id(SEARCH_TITLE_ID).text
        self.assertEqual(home_title, 'Search the UK business population')

    def assert_login_page_title(self):
        login_title = self.driver.find_element_by_id(LOGIN_TITLE_ID).text
        self.assertEqual(login_title, 'Sign in')

    def test_login(self):
        self.assert_login_page_title()
        self.input_username_password_and_login(ADMIN_USERNAME, ADMIN_PASSWORD)
        self.assertEqual(self.driver.current_url, SEARCH_URL)
        self.assert_search_page_title()

    def test_login_and_logout(self):
        self.input_username_password_and_login(ADMIN_USERNAME, ADMIN_PASSWORD)
        self.assertEqual(self.driver.current_url, SEARCH_URL)
        self.assert_search_page_title()
        self.driver.find_element_by_id(LOGOUT_BUTTON_ID).click()
        self.assert_login_page_title()

    def test_login_and_refresh(self):
        """ This is just to ensure the session continues after a refresh """
        self.input_username_password_and_login(ADMIN_USERNAME, ADMIN_PASSWORD)
        self.assert_search_page_title()
        self.assertEqual(self.driver.current_url, SEARCH_URL)
        self.driver.refresh()
        self.assertEqual(self.driver.current_url, SEARCH_URL)

    def test_invalid_credentials(self):
        self.input_username_password_and_login(INVALID_USERNAME, INVALID_PASSWORD)
        self.assertTrue('Invalid Credentials. Please try again.' in self.driver.page_source)
        self.assertEqual(self.driver.current_url, LOGIN_URL)

    def test_private_routes(self):
        """ We need to ensure that an unauthenticated user cannot get past the login page """
        self.assert_login_page_title()
        self.driver.get(SEARCH_URL)
        self.assertTrue('401 - Not Authenticated' in self.driver.page_source)
        self.assertTrue('Please login before navigating to the Home or Results pages.' in self.driver.page_source)
        self.assertEqual(self.driver.current_url, ERROR_URL)


if __name__ == '__main__':
    unittest.main()
