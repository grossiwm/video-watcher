from youtube_automator import watch
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
    jar_process = subprocess.Popen(['java', '-jar', 'jar/sniffer.jar', '192.168.25.13'])

    url = line.strip()
    watch(chrome, url, index)

    jps_process = subprocess.Popen(my_env['JAVA_HOME'] + "\\bin\jps.exe", shell=True, stdout=subprocess.PIPE)
    jps_output = subprocess.check_output(['findstr', 'sniffer'], stdin=jps_process.stdout)
    jps_process.wait
    sniffer_pid = int(jps_output.split()[0])
    subprocess.call(['taskkill', '/PID', str(sniffer_pid), '/F'])

    index += 1

chrome.close()