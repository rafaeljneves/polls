from splinter import Browser


def before_all(context):
    context.browser = Browser('chrome')
    context.server_url = 'http://localhost:8000'
    #context.browser.visit('http://localhost:8000/admin')


def after_all(context):
    context.browser.quit()