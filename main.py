from youtube_automator import watch
from system_utils import jps_path, grep, kill, sniffer_execution, sniffer_execution_env
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
import subprocess, os

my_env = os.environ.copy()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_extension('resources/extensions/AdBlocker.crx')

chrome=webdriver.Chrome(ChromeDriverManager().install(), options=options)
# Close welcome plugin screen 
chrome.switch_to.window(chrome.window_handles[0])
chrome.close()
chrome.switch_to.window(chrome.window_handles[0])

file=open('youtube_urls.txt', 'r')
Lines = file.readlines()
index=0
for line in Lines:
    jar_process = subprocess.Popen(sniffer_execution(), env=sniffer_execution_env(my_env))

    url = line.strip()
    watch(chrome, url, index)

    jps_process = subprocess.Popen(jps_path(), stdout=subprocess.PIPE)
    jps_output = subprocess.check_output(grep('sniffer'), stdin=jps_process.stdout)
    jps_process.wait
    sniffer_pid = int(jps_output.split()[0])
    subprocess.call(kill(sniffer_pid))

    index += 1

chrome.close()