from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Register.html")

#Radio Button
driver.find_element(By.XPATH,"//input[@value ='FeMale']").click()

#Checkbox and RadioButton
list = driver.find_elements(By.XPATH,"//input[@type = 'checkbox']")

for ele in list:
    val = ele.get_attribute('value')
    print(val)
    if val == 'Cricket':
        ele.click()