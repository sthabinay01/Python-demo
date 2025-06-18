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
