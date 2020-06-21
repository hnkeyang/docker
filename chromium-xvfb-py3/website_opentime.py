#!/usr/bin/python3
#
import os
import sys
from selenium import webdriver

url = os.environ.get('URL')

if url is None:
    print('000')
    sys.exit()
    
driver = webdriver.Chrome()
driver.viewportSize={'width':1024,'height':800}
driver.get(url)
driver.save_screenshot('/opt/screenshot.png')

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
loadEventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")
print(loadEventEnd - navigationStart)
