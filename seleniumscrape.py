# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options

# options = Options
# options.binary_location = '/opt/firefox/firefox'
# browser = webdriver.Firefox(options=options)
# type(browser)

################## Selenium scraper
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Firefox()

# browser.get('https://bestvalidator.xyz')
# browser.implicitly_wait(1)
# try:
#   nameinput = browser.find_element(By.ID, 'name')
#   emailinput = browser.find_element(By.ID, 'email')
#   msginput = browser.find_element(By.TAG_NAME, 'textarea')
#   nameinput.send_keys("Selenium scraping")
#   emailinput.send_keys("selenium@python.com")
#   msginput.send_keys("Python + Selenium Scraping test, Muhammadyusuf")
#   # Manually dispatch input event via JS
#   browser.execute_script("arguments[0].dispatchEvent(new Event('input'))", msginput)
#   msginput.submit()
#   print('Form submitted :)')
# except Exception as e:
#   print('Form not submitted :(')
#   print(f'Error: {e}')
