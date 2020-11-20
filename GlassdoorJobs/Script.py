import GlassdoorJobs.Elements as Elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import GlassdoorJobs.Credentials as credentials
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Jitender\PycharmProjects\JobScraping\chromedriver.exe")
driver.maximize_window()

def login(username,password):
    driver.get(Elements.HOME_PAGE)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(Elements.SIGN_IN_BUTTON).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(Elements.EMAIL_TEXTBOX).send_keys(username)
    driver.find_element_by_xpath(Elements.PASSWORD_TEXTBOX).send_keys(password)
    driver.find_element_by_xpath(Elements.LOGIN_BUTTON).click()
    time.sleep(5)

def scrap(title="Developer",type=0,location = "Bengaluru",pages=-1,):
    '''

    :param title: str - What to search for
    :param type: index of item in list [JOBS, COMPANIES, SALARIES, INTERVIEWS]
    :param location: str - Location where to search
    :param pages: str - no. of pages to scroll (-1 means all)
    :return:
    '''
    if(len(driver.find_elements_by_xpath(Elements.USLESS_OVERLAY))>0):
        driver.find_element_by_xpath(Elements.USLESS_OVERLAY).click()
    time.sleep(3)
    titleObj = driver.find_element_by_xpath(Elements.SEARCH_BAR)
    titleObj.click()
    titleObj.send_keys(title)
    time.sleep(3)
    titleObj.send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    time.sleep(3)

    typeObj = driver.find_element_by_xpath(Elements.TYPE)
    typeObj.click()
    typeListObj = driver.find_elements_by_xpath(Elements.TYPE_OPTIONS_LIST)[type]
    typeListObj.click()

    time.sleep(3)

    locationObj = driver.find_element_by_xpath(Elements.LOCATION)
    locationObj.click()
    locationObj.send_keys(Keys.CONTROL+'a'+Keys.DELETE)
    locationObj.send_keys(location)
    time.sleep(3)
    locationObj.send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    time.sleep(3)

    driver.find_element_by_xpath(Elements.SEARCH_BUTTON).click()


if __name__ == "__main__":
    login(credentials.USERNAME,credentials.PASSWORD)
    scrap(type=2)
