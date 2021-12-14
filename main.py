from youtube_automator import watch
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome=webdriver.Chrome(ChromeDriverManager().install(), options=options)

watch(chrome, 'https://www.youtube.com/watch?v=Cf_5aLm-CGs')

chrome.close()