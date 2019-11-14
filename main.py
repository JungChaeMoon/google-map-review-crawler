import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_driver_path = os.path.join(BASE_DIR, 'chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(3)

driver.get("https://www.google.com/maps/place/N%EC%84%9C%EC%9A%B8%ED%83%80%EC%9B%8C/@37.5511694,126.9860379,17z/data=!4m7!3m6!1s0x0:0x5cf8577c2e7982a5!8m2!3d37.5511694!4d126.9882266!9m1!1b1")
driver.implicitly_wait(3)

html = driver.page_source

num_of_pagedowns = 10

elem = driver.find_elements_by_class_name('section-layout.section-scrollbox.scrollable-y.scrollable-show')[-1]

while num_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.4)
    num_of_pagedowns = num_of_pagedowns -1

search_result = driver.find_elements_by_class_name('section-review-text')

review_list = []
for review in search_result:
    review_list.append(review.text)

with open('your_file.txt', 'w') as f:
    for item in review_list:
        f.write("%s\n" % item)

print(review_list)
driver.close()

