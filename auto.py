from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')


assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(by=By.CLASS_NAME, value='btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(by=By.ID, value='user-message')

user_button2 = chrome_browser.find_element(by=By.CSS_SELECTOR, value='#get-input')
print(user_button2)
user_message.clear()
user_message.send_keys('I am Extra cool')

show_message_button.click()
output_message = chrome_browser.find_element(by=By.ID, value='display')

assert 'I am Extra cool' in output_message.text

chrome_browser.close()