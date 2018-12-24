from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Create your tests here.


class UserTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:\Program Files (x86)\Google\ChromeDriver\chromedriver.exe')
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_user_tests_url_shortener(self):
        """
        user creates a shortened url, and visits the site contained therein
        """

        # user is on the index page
        home_page = self.browser.get(self.live_server_url + '')

        # user sees the page header
        brand_element = self.browser.find_element_by_css_selector('#page-header')

        # user types a url into the textbox an submits the form.

        url_shortening_form = self.browser.find_element_by_id('url-shortening-form')
        url_shortening_form.find_element_by_id('id_user_url').send_keys('https://www.google.com/')
        url_shortening_form.find_element_by_id('id_user_email').send_keys('christopher.siegel@dmu.edu')
        url_shortening_form.find_element_by_class_name('submit').click()

        # they are taken back to the index page and their url has been shortened and displayed

        self.assertEqual(self.browser.current_url, self.live_server_url + '/')

        shortened_url = self.browser.find_element_by_id('shortened_url')

        # they click on their shortened url and are taken to that page.
        shortened_url.click()
        new_tab = self.browser.window_handles[1]
        self.browser.switch_to_window(new_tab)
        self.assertEqual(self.browser.current_url, 'https://www.google.com/')
