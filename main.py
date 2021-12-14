from youtube_automator import watch
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome=webdriver.Chrome(ChromeDriverManager().install(), options=options)

file=open('youtube_urls.txt', 'r')
Lines = file.readlines()

for line in Lines:
    url = line.strip()
    watch(chrome, url)

chrome.close()