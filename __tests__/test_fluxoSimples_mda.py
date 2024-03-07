# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFluxoSimplesMDA():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_fluxoSimplesMDA(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1472, 931)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    assert self.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name").text == "Sauce Labs Backpack"
    self.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_details_name").text == "Sauce Labs Backpack"
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_details_price").text == "$29.99"
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").text == "Add to cart"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").text == "Remove"
    assert self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "1"
    self.driver.find_element(By.LINK_TEXT, "1").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack"
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()
