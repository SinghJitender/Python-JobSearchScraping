HOME_PAGE = "https://www.glassdoor.co.in/"
SIGN_IN_BUTTON = "//a[@data-ga-lbl='Sign In']"
EMAIL_TEXTBOX = "//input[@id='userEmail']"
PASSWORD_TEXTBOX = "//input[@id='userPassword']"
LOGIN_BUTTON = "//button[@name='submit']"

#When Logged In
SEARCH_BAR = "//input[@id='sc.keyword']"
TYPE = "//form[@id='scBar']//div//div[2]"
TYPE_OPTIONS_LIST = "//form[@id='scBar']//div[2]//div//div[contains(@class,'dropdownOptions ')]//div[@class='dropDownOptionsContainer']//ul//li"
LOCATION = "//input[@id='sc.location']"
SEARCH_BUTTON = "//button[@type='submit']"

USLESS_OVERLAY = "//div[contains(@class,'gd-ui-overlay')]"
USELESS_SPAN = "//div[@id='JAModal']//span[@alt='Close']"

#Scrap data
MAIN_TEXT = "//div[@class='jobDescriptionContent desc']"
LIST_OF_ITEMS = "//ul[contains(@class,'jlGrid')]//li"
LIST_JOB_LINK = "//ul[contains(@class,'jlGrid')]//li//a[@class='jobLink']"

#Each Listing
COMPANY_NAME = "(//div[@class='employerName'])[1]"
RATINGS = "(//div[@class='employerName']//span)[1]"
TITLE = "(//div[@class='title'])[1]"
JOB_LOCATION = "(//div[@class='location'])[1]"

