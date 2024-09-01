import os
import re
import time
import json
import nltk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

words = open('words_new.txt').read().split('\n')[:-1]
done = os.listdir('words')
for word in words:
    if word + '.txt' in done:
        continue
    driver.refresh()
    all_links = []
    search_area = driver.find_elements(By.CLASS_NAME, 'MainSearchField')[0]
    search_area.send_keys(word)
    time.sleep(20)
    while True:
        time.sleep(5)
        page_links = [link.get_attribute('href') for link in driver.find_elements(By.CLASS_NAME, 'CardLink')]
        if page_links[0] in all_links:
            break
        all_links = all_links + page_links
        try:
            next_page = driver.find_elements(By.CLASS_NAME, 'r-page-link')[-2]
            next_page.send_keys(Keys.ENTER)
        except:
            break
        time.sleep(5)
    with open('words/' + word + '.txt', 'w') as f:
        for link in all_links:
            x = f.write(link + '\n')


driver.close()

b = os.listdir('words')
b.sort()
k = 0
for i in b:
    print(i, len(open('words/' + i).read().split('\n')[:-1]))
    k = k + len(open('words/' + i).read().split('\n')[:-1])

print(k)
