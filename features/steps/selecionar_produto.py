from behave import given, when, then
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "login-button").click()

@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"

@then(u'exibe mensagem {mensagem}')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem
