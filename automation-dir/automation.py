from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='chromedriver')
chrome_browser = webdriver.Chrome('chromedriver')

chrome_browser.maximize_window()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')


# popup = chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOL')
show_message_button.click()

stay_open = input()
