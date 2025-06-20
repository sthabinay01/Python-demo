from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Index.html")

'''locators:
By.ID
By.NAME
By.CLASS_NAME
BY.TAG_NAME
BY.LINK_TEXT
BY.PARTIAL_LINK_TEXT
BY.CSS_SELECTOR
BY>XPATH'''

email_text = driver.find_element(By.ID,'email')
email_text.send_keys("ttest@gmail.com")
driver.find_element(By.ID,'enterimg').click()

#XPATH
# synteax - //tagname[@attribute = 'value'] or //*[@attribute = 'value']
#//input[@placeholder = 'First Name']

#text
#label[text()='Full Name*']

#contains
#//label[contains(text(),'Full Name')]

#index
#//label[2]

#or & AND
#//*[@placeholder = 'First Name' and @ng-model="FirstName"]

