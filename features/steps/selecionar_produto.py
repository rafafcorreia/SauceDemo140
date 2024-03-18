from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(usuario)
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(senha)
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()


@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    time.sleep(2)

@when(u'preencho os campos de login com {standard_user} e {secret_sauce}')
def step_impl(context, standard_user, secret_sauce):
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(standard_user)
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(secret_sauce)
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()

