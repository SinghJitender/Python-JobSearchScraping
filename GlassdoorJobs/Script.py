import GlassdoorJobs.Elements as Elements
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\Jitender\PycharmProjects\JobScraping\chromedriver.exe")

def login(username,password):
    driver.get(Elements.HOME_PAGE)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(Elements.SIGN_IN_BUTTON).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(Elements.EMAIL_TEXTBOX).send_keys(username)
    driver.find_element_by_xpath(Elements.PASSWORD_TEXTBOX).send_keys(password)
    driver.find_element_by_xpath(Elements.LOGIN_BUTTON).click()

if __name__ == "__main__":
    login("jitu.singh95@gmail.com","")
