import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):

     self.driver.find_element(By.NAME,"search").send_keys("HP")
     self.driver.find_element(By.XPATH,"//button[contains(@class,'btn-default btn-lg')]").click()
     assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()


    def test_search_for_an_invalid_product(self):

     self.driver.find_element( By.NAME, "search" ).send_keys( "Honda" )
     self.driver.find_element( By.XPATH, "//button[contains(@class,'btn-default btn-lg')]" ).click()
     self.expected_text=self.driver.find_element(By.XPATH,"//input[@id='button-search']//following-sibling::p").text
     assert self.expected_text.__eq__("There is no product that matches the search criteria.")


    def test_search_without_product(self):

     self.driver.find_element( By.XPATH, "//button[contains(@class,'btn-default btn-lg')]" ).click()
     time.sleep(4)
     expected_text=self.driver.find_element(By.XPATH,"//input[@id='button-search']//following-sibling::p").text
     assert expected_text.__eq__("There is no product that matches the search criteria.")

