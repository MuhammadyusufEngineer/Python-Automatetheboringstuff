from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random

target_tg_profiles = ['</> Murtazoxon', '</> Abdulahad oka']

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
options.profile = firefox_profile

driver = webdriver.Firefox(options=options)
driver.get('https://web.telegram.org/a')
print("Opening Telegram Web...")

# Wait for the page to load completely
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    print("Telegram loaded successfully")
except TimeoutException:
    print("Timeout waiting for page to load")
    driver.quit()
    exit()

human_delay(5, 8)  # Give more time for the app to initialize

wait = WebDriverWait(driver, 15)  # Increasing wait time

for i, profile_name in enumerate(target_tg_profiles):
    try:
        print(f"\nAttempting to message: {profile_name}")
        
        # Click on search - different ways to find it
        try:
            # First try the ID
            search_box = wait.until(EC.element_to_be_clickable((By.ID, "telegram-search-input")))
        except:
            try:
                # Try by placeholder text
                search_box = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@placeholder='Search' or @placeholder='Search...' or contains(@placeholder, 'Search')]")))
            except:
                # Try by class
                search_box = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".SearchInput input")))
        
        search_box.clear()  # Clear any previous search
        search_box.click()
        human_delay()
        human_typing(search_box, profile_name)
        print(f"Searching for: {profile_name}")
        
        # Press Enter to initiate search
        search_box.send_keys(Keys.ENTER)
        human_delay(3, 5)
        
        # Wait and look for search results with multiple selector attempts
        try:
            # Try different selectors for finding the profile in search results
            selectors = [
                # By list item containing the name
                f"//div[contains(@class, 'ListItem') and contains(., '{profile_name}')]",
                # By chat item
                f"//div[contains(@class, 'chat-item') and contains(., '{profile_name}')]",
                # By search result
                f"//div[contains(@class, 'search-result') and contains(., '{profile_name}')]",
                # More general selector - any element containing the exact profile name
                f"//*[text()='{profile_name}']",
                # By partial text match
                f"//*[contains(text(), '{profile_name}')]"
            ]
            
            found = False
            for selector in selectors:
                try:
                    print(f"Trying selector: {selector}")
                    found_profile = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    found = True
                    break
                except:
                    continue
            
            if not found:
                print(f"Could not find profile: {profile_name}, trying fallback")
                # Fallback: just click on the first search result
                found_profile = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".search-result, .ListItem, .chat-item")))
            
            print(f"Found profile element, clicking...")
            human_delay(1, 2)
            found_profile.click()
            human_delay(2, 3)
            
            # Find message input - try multiple selectors
            message_selectors = [
                "//div[@id='editable-message-text']", 
                "//div[@role='textbox']",
                "//div[contains(@class, 'composer')]//div[@role='textbox']",
                "//div[contains(@class, 'input-message-input')]"
            ]
            
            found = False
            for selector in message_selectors:
                try:
                    message_box = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    found = True
                    break
                except:
                    continue
                    
            if not found:
                print(f"Could not find message box for {profile_name}")
                continue
                
            human_delay(1, 2)
            message_box.click()
            human_typing(message_box, "Hello! This is a selenium test message =)")
            print("Typed message")
            human_delay(1, 2)
            
            # Try different ways to find send button
            send_selectors = [
                "//button[@name='Send Message']",
                "//button[@aria-label='Send Message']",
                "//button[contains(@class, 'send')]",
                "//button[contains(@class, 'Button') and contains(@class, 'send')]"
            ]
            
            found = False
            for selector in send_selectors:
                try:
                    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    found = True
                    break
                except:
                    continue
                    
            if not found:
                # Try sending with keyboard shortcut instead
                print("Send button not found, trying Enter key")
                message_box.send_keys(Keys.ENTER)
            else:
                send_button.click()
                
            print(f"Message sent to {profile_name}")
            human_delay(2, 3)
            
        except Exception as e:
            print(f"Error while processing {profile_name}: {str(e)}")
            
    except Exception as e:
        print(f"Failed to process {profile_name}: {str(e)}")

print('Done =)')
driver.quit()