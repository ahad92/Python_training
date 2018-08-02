# -*- coding: utf-8 -*-

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time

class test_add_patient(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_add_patient(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.create_patient(driver)
        self.logout(driver)

    def logout(self, driver):
        # logout
        driver.find_element_by_xpath("//i").click()
        driver.find_element_by_link_text(u"Выйти").click()

    def create_patient(self, driver):
        # open patient page
        driver.find_element_by_link_text(u"Пациенты").click()
        # fill patient form
        driver.find_element_by_link_text(u"Добавить пациента").click()
        driver.find_element_by_id("full_name").click()
        driver.find_element_by_id("full_name").clear()
        driver.find_element_by_id("full_name").send_keys("Patient Test Two")
        driver.find_element_by_id("date_of_birth").click()
        driver.find_element_by_id("date_of_birth").clear()
        driver.find_element_by_id("date_of_birth").send_keys("27.10.1977")
        driver.find_element_by_id("comment").click()
        time.sleep(1)
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("mail1@test.if")
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("89600087485")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("qwerty")
        driver.find_element_by_id("password_confirmation").click()
        driver.find_element_by_id("password_confirmation").clear()
        driver.find_element_by_id("password_confirmation").send_keys("qwerty")
        driver.find_element_by_id("select2-doctor-container").click()
        driver.find_element_by_xpath("/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[45]").click()
        driver.find_element_by_id("comment").click()
        driver.find_element_by_id("comment").clear()
        driver.find_element_by_id("comment").send_keys("тестовые комментарии о пациенте ")
        # submit patient creation
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def login(self, driver):
        # login
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("ahad92@mail.ru")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def open_home_page(self, driver):
        # open home page
        driver.get("https://t-admin.ibolit.pro/login")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
'''
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
'''

if __name__ == "__main__":
    unittest.main()
