from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup opitons
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Selenium 4.0 - load webdriver
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(1)

url = 'https://nsu.ac.kr/?m1=page%25&menu_id=138%25'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser') 

sival = driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[5]/div/div[3]/div[3]/div[5]/div[2]').text
print(sival)
driver.quit() 