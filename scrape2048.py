from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random, time

arrows = [Keys.ARROW_UP, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_RIGHT]
driver = webdriver.Firefox()
driver.get('https://play2048.co/')

time.sleep(2)

print('Starting 2048 automation...')
body = driver.find_element(By.TAG_NAME, 'body')

for i in range(200):
  print(f'Clicked {i+1} times...')
  time.sleep(0.2)
  body.send_keys(random.choice(arrows))

print('Done!')