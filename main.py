from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(r'/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = 'Poliumvirato Poli'
msg = 'ciao raga'
time.sleep(20)
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"][@dir="ltr"][@spellcheck="true"]')
msg += '\n'

while True:
    msg_box.send_keys(msg)
    time.sleep(0.1)