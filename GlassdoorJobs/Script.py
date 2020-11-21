import GlassdoorJobs.Elements as Elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import GlassdoorJobs.Credentials as credentials
import time
import logging
import xlsxwriter
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)
driver = webdriver.Chrome(executable_path=r"C:\Users\Jitender\PycharmProjects\JobScraping\chromedriver.exe")
driver.maximize_window()


def login(username, password):
    driver.get(Elements.HOME_PAGE)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(Elements.SIGN_IN_BUTTON).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(Elements.EMAIL_TEXTBOX).send_keys(username)
    driver.find_element_by_xpath(Elements.PASSWORD_TEXTBOX).send_keys(password)
    driver.find_element_by_xpath(Elements.LOGIN_BUTTON).click()
    time.sleep(5)


def searchFor(title="Developer", type=0, location="Bengaluru", pages=-1, ):
    '''
    :param title: str - What to search for
    :param type: index of item in list [JOBS, COMPANIES, SALARIES, INTERVIEWS]
    :param location: str - Location where to search
    :param pages: str - no. of pages to scroll (-1 means all)
    :return:
    '''
    if (len(driver.find_elements_by_xpath(Elements.USLESS_OVERLAY)) > 0):
        driver.find_element_by_xpath(Elements.USLESS_OVERLAY).click()

    typeObj = driver.find_element_by_xpath(Elements.TYPE)
    typeObj.click()
    typeListObj = driver.find_elements_by_xpath(Elements.TYPE_OPTIONS_LIST)[type]
    typeListObj.click()

    locationObj = driver.find_element_by_xpath(Elements.LOCATION)
    locationObj.click()
    locationObj.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
    locationObj.send_keys(location)
    time.sleep(3)
    locationObj.send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    time.sleep(3)
    titleObj = driver.find_element_by_xpath(Elements.SEARCH_BAR)
    titleObj.click()
    titleObj.send_keys(title)
    time.sleep(3)
    titleObj.send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    time.sleep(3)

    # driver.find_element_by_xpath(Elements.SEARCH_BUTTON).click()

    time.sleep(5)
    if (type in [0, 1]):
        scarp()


def scarp():
    '''
    Fetches data for searched items from glassdoor
    :return: None
    '''
    wb = xlsxwriter.Workbook("Job_Search_%s.xlsx" % str(datetime.datetime.now().strftime("%Y_%m_%d_%I_%M_%p")))
    sheet = wb.add_worksheet()
    sheet.write_row(0,0,data = ["ID", "Title", "Company", "Location" "Ratings", "Link", "Match Percentage"])

    listOfItems = driver.find_elements_by_xpath(Elements.LIST_OF_ITEMS)
    listOfLinks = driver.find_elements_by_xpath(Elements.LIST_JOB_LINK)
    logging.info("len of listOfItems %s" % len(listOfItems))

    itemPos = 0
    for item in listOfItems:
        link = listOfLinks[itemPos].get_attribute("href")
        item.click()
        if driver.find_elements_by_xpath(Elements.USELESS_SPAN):
            driver.find_element_by_xpath(Elements.USELESS_SPAN).click()
            time.sleep(1)

        companyObj = driver.find_element_by_xpath(Elements.COMPANY_NAME)
        if len(driver.find_elements_by_xpath(Elements.RATINGS)) > 0:
            ratingObj = driver.find_element_by_xpath(Elements.RATINGS)
            rating = ratingObj.text
        else:
            rating = None
        jobTitleObj = driver.find_element_by_xpath(Elements.TITLE)
        jobLocationObj = driver.find_element_by_xpath(Elements.JOB_LOCATION)
        mainTextObj = driver.find_element_by_xpath(Elements.MAIN_TEXT)
        value = mainTextObj.text
        logging.info("%s \n\n" % value)
        sheet.write_row(itemPos+1,0,data = [itemPos, jobTitleObj.text, companyObj.text, jobLocationObj.text, rating, link, "0"])
        itemPos += 1

    wb.close()


if __name__ == "__main__":
    logging.info("Logs Working")
    login(credentials.USERNAME, credentials.PASSWORD)
    searchFor()
