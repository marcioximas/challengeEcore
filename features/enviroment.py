def before_all(context):
    context.driver = None

def after_all(context):
    if context.driver:
        context.driver.quit()
