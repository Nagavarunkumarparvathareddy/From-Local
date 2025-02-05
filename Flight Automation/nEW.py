from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import time

# Path to Edge WebDriver
edge_driver_path = "C:\\webdrivers\\msedgedriver.exe"

# Initialize WebDriver
service = Service(edge_driver_path)
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Edge(service=service, options=options)
driver.implicitly_wait(10)

# Initialize WebDriverWait
wait = WebDriverWait(driver, 20)

# Function to select a location (From/To)
def select_location(location_input_xpath, suggestion_xpath, city_name):
    try:
        # Click on the location field
        location_input = wait.until(EC.element_to_be_clickable((By.XPATH, location_input_xpath)))
        location_input.click()

        # Input the city name
        input_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @value='']")))
        input_box.clear()
        input_box.send_keys(city_name)

        # Wait and click on the suggestion
        suggestion = wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath)))
        suggestion.click()
        print(f"{city_name} selected from the suggestions!")
    except Exception as e:
        print(f"Error while selecting {city_name}: {e}")

# Function to select a date
def select_date(date_xpath):
    try:
        # Open the calendar
        calendar_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='sc-12foipm-8 eXKWBG fswDownArrow']")))
        calendar_input.click()
        print("Calendar opened.")

        # Wait for the calendar to be visible
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='DayPicker']")))

        # Click on the desired date
        date_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", date_to_select)
        date_to_select.click()
        print("Date selected successfully!")
    except Exception as e:
        print(f"Error while selecting date: {e}")

try:
    # Navigate to Goibibo's website
    driver.get("https://www.goibibo.com/")

    # Select "From" location
    from_location_xpath = "//p[@class='sc-12foipm-6 erPfRs' and text()='Enter city or airport']"
    from_suggestion_xpath = "//div[@class='sc-12foipm-32 jVTqNw']//p[contains(text(), 'Rajiv Gandhi International Airport')]"
    select_location(from_location_xpath, from_suggestion_xpath, "Hyderabad")

    # Select "To" location
    to_suggestion_xpath = "//div[@class='sc-12foipm-32 jVTqNw']//p[contains(text(), 'Indira Gandhi International Airport')]"
    select_location("//input[@type='text' and @value='']", to_suggestion_xpath, "Delhi")

    # Select a date
    date_xpath = "//div[@aria-label='Mon Jan 06 2025']"
    select_date(date_xpath)

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    # Ensure resources are released
    time.sleep(5)  # Allow time to observe before closing
    driver.quit()
