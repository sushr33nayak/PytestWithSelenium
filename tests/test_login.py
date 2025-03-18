import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.variables import Variables


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin :
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH,"//a[text()='Login']").click()
        assert self.driver.find_element(By.XPATH,"//h2[text()='Returning Customer']").is_displayed()

    def test_login_with_invalid_credentials(self):
        variable=Variables()
        self.driver.find_element(By.XPATH,"//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH,"//a[text()='Login']").click()
        self.driver.find_element(By.NAME,"email").send_keys(variable.email)
        self.driver.find_element( By.NAME, "password" ).send_keys(variable.password)
        time.sleep(3)
        self.driver.find_element( By.XPATH, "//input[@value='Login']" ).click()
        text_a= self.driver.find_element( By.XPATH, "//div[@class='alert alert-danger alert-dismissible']" ).text
        text_b="Warning: No match for E-Mail Address and/or Password."
        assert text_a.__eq__(text_b)
