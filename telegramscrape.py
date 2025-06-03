from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

target_tg_profiles = ['Jahongir Bro CompassX', '</> Murtazoxon', '</> Abdulahad oka', 'HBAI UZB']

def human_delay(min_time=0.5, max_time=1.5):
  time.sleep(random.uniform(min_time, max_time))

def human_typing(element, text):
  for char in text:
    time.sleep(random.uniform(0.05, 0.15))
    element.send_keys(char)

# using existing profile in order to avoid temporary browser profile
existing_profile_path = '/home/engineer/.mozilla/firefox/wz8trmwk.default-release'
options = Options()
firefox_profile = FirefoxProfile(existing_profile_path)
# firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile

driver = webdriver.Firefox(options=options)
driver.get('https://web.telegram.org/a')
human_delay(3, 5)

wait = WebDriverWait(driver, 10)

for i in range(len(target_tg_profiles)):
  search_box = driver.find_element(By.ID, "telegram-search-input") ####### CHANGE XPATH
  search_box.click()
  human_delay()
  human_typing(search_box, target_tg_profiles[i])
  
  human_delay(3,5)

  found_profile = driver.find_element(By.XPATH, 
                                      "//div[@id='LeftColumn']//div[@class='LeftSearch']//div[contains(@class, 'Transition_slide-active')]//div[contains(@class, 'Transition_slide-active')]//div[contains(@class, 'Transition_slide-active')]//div[contains(@class, 'search-result')]//h3[@class='fullName']") ######## CHANGE XPATH
  print(f'FOUND PROFILE: {found_profile}')
  human_delay(1,2)
  found_profile.click() 
  human_delay()

  message_box = driver.find_element(By.XPATH, "//div[@id='editable-message-text']") ####### CHANGE XPATH
  human_delay(1,2)
  message_box.click() 
  human_typing(message_box, "Hello! This is a selenium test message =)")
  human_delay()

  send_button = driver.find_element(By.XPATH, "//button[@name='Send Message']")
  human_delay(1,2)
  send_button.click()
  human_delay()

print('Done =)')
  
