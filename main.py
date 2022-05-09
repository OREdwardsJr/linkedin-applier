from imports import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Keys
load_dotenv()
EMAIL = os.environ.get("EMAIL")
PW = os.environ.get("PW")

# Config
options = FirefoxOptions()
driver = webdriver.Firefox(service=Service(
    GeckoDriverManager().install()), options=options)


def login():
    login_url = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account"
    driver.get(login_url)

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    username.send_keys(EMAIL)

    password = driver.find_element(By.ID, "password")
    password.send_keys(PW)

    login = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    login.click()

    return f"Successfully logged in!"


login()

'''
Criteria:
    - Search: "software engineer python"
    - Experience: "internship, entry-level, associate"
    - Easy Apply: selected
Add "&start=25" to the end of jobs_url to go to next page. Additional pages increment by 25
'''
# Jobs posted in the last week. There's typically ~120 postings
jobs_url = "https://www.linkedin.com/jobs/search/?currentJobId=3060295800&f_AL=true&f_E=1%2C2%2C3&f_PP=104116203&f_TPR=r604800&geoId=103644278&keywords=software%20engineer%20python&location=United%20States&sortBy=R"

# Remote jobs in the last week
#jobs_url = "https://www.linkedin.com/jobs/search/?f_AL=true&f_PP=104116203&f_TPR=r86400&geoId=103644278&keywords=software%20engineer%20python&location=United%20States&sortBy=R"


driver.get(jobs_url)

jobs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, "jobs-search-results__list-item")))
time.sleep(10)
jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for job in jobs:
    print(job.text)

driver.quit()
print("done")


'''
Note to self:
To go to a new page you can just iterate by 25.
EG:
page1: doesn't have a start at the end
page2: url + "&start=25"
page3: url + "&start=50"
page4: url + "&start=75"
etc...

For determining whether there's a "Next", "Review", or "Submit" then you should be able to access the text content from the below class:
class="artdeco-button__text"
'''

'''
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
lists = soup.find_all("div", class_="base-card")
print(len(lists))
'''
