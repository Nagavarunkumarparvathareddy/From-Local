from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Edge(options=options)
driver.implicitly_wait(10)

# Navigate to Goibibo's website
driver.get("https://www.goibibo.com/")

# Initialize WebDriverWait
wait = WebDriverWait(driver, 20)

try:
    # Wait for the "From" location input field to be clickable
    from_location = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='sc-12foipm-6 erPfRs' and text()='Enter city or airport']")))
    from_location.click()

    print("From location clicked successfully!")

    from_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @value='']"))) # Targeting input with type='text'
    from_input.clear() # Clear the input field before typing
    from_input.send_keys("Hyderabad")
    time.sleep(3) # Wait for suggestions to load

    # Wait for the suggestions to appear and click the suggestion that matches the city
    suggestion_xpath = "//div[@class='sc-12foipm-32 jVTqNw']//p[contains(text(), 'Rajiv Gandhi International Airport')]"
    first_suggestion = wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath)))
    first_suggestion.click()
    print("Hyderabad selected from the suggestions!")

    # --- Now for the "To" location ---

    # Wait for the "To" location input field to be clickable
    to_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @value='']"))) # Targeting input with type='text'
    to_input.clear() # Clear the input field before typing
    to_input.send_keys("Delhi")
    time.sleep(3) # Wait for suggestions to load

    # Wait for the suggestions to appear and click the suggestion that matches the city
    to_suggestion_xpath = "//div[@class='sc-12foipm-32 jVTqNw']//p[contains(text(), 'Indira Gandhi International Airport')]"
    to_first_suggestion = wait.until(EC.element_to_be_clickable((By.XPATH, to_suggestion_xpath)))
    to_first_suggestion.click()
    print("Delhi selected from the suggestions!")

    # Wait for the calendar input field to be clickable and click to open the calendar
    calendar_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='sc-12foipm-8 eXKWBG fswDownArrow']")))
    calendar_input.click()
    print("Calendar opened.")

    # Wait for the calendar to be visible
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='DayPicker']")))

    # Ensure the calendar is loaded completely before moving forward
    time.sleep(2) # Give time for any async processes to complete

    # Locate the specific date, here January 6, 2025
    date_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Mon Jan 06 2025']")))

    # Scroll the date element into view before clicking
    driver.execute_script("arguments[0].scrollIntoView(true);", date_to_select)
    time.sleep(1) # Optional: Wait for a moment to ensure the element is in view

    # Use JavaScript to click the date if it's still not clickable
    driver.execute_script("arguments[0].click();", date_to_select)
    print("Date Mon Jan 06 2025 selected successfully!")

    # Wait for any UI changes after selecting the date
    time.sleep(2) # Adjust this time as necessary for UI updates

except Exception as e:
    print(f"Error: {e}")

finally:
  time.sleep(5)
  driver.quit()