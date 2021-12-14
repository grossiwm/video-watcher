from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time

def get_secs(txt):
    arr = txt.split(':')
    secs = int(arr[0])*60 + int(arr[1])
    return secs

def watch(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)


    button=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'button.ytp-play-button')))
    button.click()

    duration_div=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'span.ytp-time-duration')))
    duration = get_secs(duration_div.text)
    time.sleep(duration)


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome=webdriver.Chrome(ChromeDriverManager().install(), options=options)

watch(chrome, 'https://www.youtube.com/watch?v=Cf_5aLm-CGs')

chrome.close()