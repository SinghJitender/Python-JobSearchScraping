from selenium import webdriver

searchBox = "//div[@class='inpWrap']//input[@type='text' and @name='keyword']"
searchButton = "//div[@class='search-btn']//button"
serachJob = "Developer"

#filters
location =""
salary = ""
experience = ""
postedby = ""

driver = webdriver.Chrome()
driver.get("https://www.naukri.com")
driver.find_element_by_xpath(searchBox).send_keys(serachJob)
driver.find_element_by_xpath(searchButton).click()
print(driver.page_source)
#driver.close()