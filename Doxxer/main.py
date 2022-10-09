from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

name = input("Enter a name: ")
address = input("Enter a City, State, or Zipcode: ")

driver.get('https://www.truepeoplesearch.com/')


search = driver.find_element(By.ID, "id-m-n")

search.send_keys(name)

search2 = driver.find_element_by_id("id-d-loc-name")
search2.send_keys(address)

search.send_keys(Keys.RETURN)

time.sleep(5)

main = driver.find_element_by_class_id("col-md-8")

print(main)


