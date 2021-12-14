from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time

def getSecs(txt):
    arr = txt.split(':')
    secs = int(arr[0])*60 + int(arr[1])
    return secs


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome=webdriver.Chrome(ChromeDriverManager().install(), options=options)
chrome.get(URL)
wait = WebDriverWait(chrome, 10)


button=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'button.ytp-play-button')))
button.click()

duration_div=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'span.ytp-time-duration')))
duration = getSecs(duration_div.text)
print(duration)
time.sleep(duration)

chrome.close()