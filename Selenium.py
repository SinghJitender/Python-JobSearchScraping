from selenium import webdriver

searchBox = "//div[@class='inpWrap']//input[@type='text' and @name='keyword']"
searchButton = "//div[@class='search-btn']//button"
searchedJobTitle = "//div[@class='list']//a[contains(@class,'fw')]"

#What Job to search for
serachJob = "Developer"

#filters
location =""
salary = ""
experience = ""
postedby = ""

driver = webdriver.Chrome()

#Script only works on naukri.com
driver.get("https://www.naukri.com")

driver.find_element_by_xpath(searchBox).send_keys(serachJob)
driver.find_element_by_xpath(searchButton).click()
driver.implicitly_wait(5)
list = driver.find_elements_by_xpath(searchedJobTitle)
print(len(list))
s = list[0].get_attribute("href")
print(s)
import requests
r = requests.get(s)
print(r)
#print(driver.page_source)
from bs4 import BeautifulSoup
c = BeautifulSoup(r.text,features="html.parser")
print(c)
#print(r.text)
#driver.close()