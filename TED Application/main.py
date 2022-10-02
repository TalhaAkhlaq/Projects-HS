from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

topic = input("Enter the topic you want to search: ")

driver.get('https://www.ted.com/talks%22%27')
print(driver.title)

search = driver.find_element(By.NAME, "q")
search.send_keys(topic)
search.send_keys(Keys.RETURN)


link = driver.find_element(By.CLASS_NAME, 'search__result__visible-url')
link.click()

time.sleep(2)

link2 = driver.find_element(By.CLASS_NAME, 'css-8khdsj')
link2.click()