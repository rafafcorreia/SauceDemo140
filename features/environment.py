from selenium import webdriver

def before_scenario(context, scenario):

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)

    print('Passo A - Antes de Tudo')

def after_scenario(context, scenario):
    
    context.driver.quit()

    print('Passo Z - Depois de Tudo')