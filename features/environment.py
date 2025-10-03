from utils.driver import create_driver

def before_all(context):
    context.driver = create_driver()

def after_all(context):
    context.driver.quit()