from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

def get_secs(txt):
    arr = txt.split(':')
    secs = int(arr[0])*60 + int(arr[1])
    return secs

def watch(driver, url, index):
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    if (index == 0):
        button=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'button.ytp-play-button')))
        button.click()

    duration_div=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'span.ytp-time-duration')))
    duration = get_secs(duration_div.text)
    print(f"sleeping for {duration} seconds")
    time.sleep(duration)