# -*- coding: utf-8 -*-

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time

from threading import Thread

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://t-admin.ibolit.pro/login")
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("ahad92@mail.ru")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Пациенты").click()
        driver.find_element_by_link_text(u"Добавить пациента").click()
        driver.find_element_by_id("full_name").click()
        driver.find_element_by_id("full_name").clear()
        driver.find_element_by_id("full_name").send_keys("Patient Test Two")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("mail1@test.if")
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("89600087485")
        time.sleep(1)
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("qwerty")
        driver.find_element_by_id("password_confirmation").click()
        driver.find_element_by_id("password_confirmation").clear()
        driver.find_element_by_id("password_confirmation").send_keys("qwerty")
        driver.find_element_by_id("select2-doctor-container").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[8]").click()
        driver.find_element_by_id("comment").click()
        driver.find_element_by_id("comment").clear()
        driver.find_element_by_id("comment").send_keys("тестовые комментарии о пациенте ")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//i").click()
        driver.find_element_by_link_text(u"Выйти").click()

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
