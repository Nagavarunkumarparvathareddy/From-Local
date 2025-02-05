import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Set up Selenium WebDriver (Ensure to download the ChromeDriver and set its path)
service = Service("C:\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Function to close popup if present
def close_popup():
    try:
        popup_close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/span/span"))
        )
        popup_close_button.click()
        print("Popup closed successfully.")
    except Exception as e:
        print("No popup found or unable to close: ", e)

# Function to launch the Goibibo website and search for flights
def search_flights(from_location, to_location, departure_date):
    driver.get("https://www.goibibo.com/")

    # Close popup if present
    close_popup()

    # Wait for the Flights tab to load and click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/header/ul/li[1]/a/span[2]"))).click()

    # Enter From Location
    from_location = 'Mumbai (BOM)'
    from_input = driver.find_element(By.XPATH, "/html/body/div/div[5]/div/div/div[2]/div[1]/div/div[2]/div/input")
    from_input.send_keys(from_location)
    time.sleep(2)
    from_input.send_keys(Keys.ENTER)

    # Enter To Location
    to_location = 'Hyderabad (HYD)'
    to_input = driver.find_element(By.XPATH, "/html/body/div/div[5]/div/div/div[2]/div[2]/div/div[2]/div/input")
    to_input.send_keys(to_location)
    time.sleep(2)
    to_input.send_keys(Keys.ENTER)

    # Enter Departure Date
    date_input = driver.find_element(By.XPATH, "/html/body/div/div[5]/div/div/div[2]/div[3]/div/p[1]")
    date_input.click()
    selected_date = driver.find_element(By.XPATH, f"//p[contains(text(), \"{departure_date.split('-')[2]} {departure_date.split('-')[1][0:3]}'{departure_date.split('-')[0][2:]}\")]")
    selected_date.click()

    # Click Search Button
    search_button = driver.find_element(By.XPATH, "/html/body/div/div[5]/div/div/div[4]/span")
    search_button.click()

# Function to apply filters (1 Stop and Price Range)
def apply_filters(price_min, price_max):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "/html/body/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div/div[4]/div[1]/span")))

    # Filter by 1 Stop
    stop_filter = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[5]/div/div[2]/label[2]/span")
    stop_filter.click()
    time.sleep(2)

    # Filter by Price Range
    price_slider = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[7]/div/div[2]/div[1]/div")
    # Adjust the price slider dynamically (This might require JavaScript execution based on the UI)
    left_slider = driver.find_element(By.XPATH,  " /html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[7]/div/div[2]/div[1]/div/div[4]") # Adjust XPath as needed
    right_slider = driver.find_element(By.XPATH, " /html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[7]/div/div[2]/div[1]/div/div[5]")  # Adjust XPath as needed
    driver.execute_script("arguments[0].style.left = '20%';", left_slider)
    driver.execute_script("arguments[0].style.left = '70%';", right_slider)
    time.sleep(2)

# Function to verify and read flight details
def fetch_filtered_flights():
    flight_data = []

    # Wait for the filtered results to load
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fltHpyCard")))

    flights = driver.find_elements(By.CLASS_NAME, "fltHpyCard")
    for flight in flights:
        try:
            stops = flight.find_element(By.CLASS_NAME, "stop-info").text
            if "1 Stop" not in stops:
                continue

            airline = flight.find_element(By.CLASS_NAME, "airline-info").text
            price = flight.find_element(By.CLASS_NAME, "price").text.replace("Rs", "").replace(",", "").strip()
            locations = flight.find_element(By.CLASS_NAME, "route").text

            flight_data.append({
                "Airline": airline,
                "Price (Rs)": int(price),
                "Route": locations
            })
        except Exception as e:
            print(f"Error reading flight: {e}")

    return flight_data

# Function to save data to Excel
def save_to_excel(flight_data, filename):
    df = pd.DataFrame(flight_data)
    df_sorted = df.sort_values(by=["Airline", "Price (Rs)"])
    df_sorted.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Main script execution
if __name__ == "__main__":
    try:
        search_flights("Mumbai", "Delhi", "2025-01-10")
        apply_filters(4000, 8000)

        flights = fetch_filtered_flights()
        save_to_excel(flights, "filtered_flights.xlsx")

    finally:
        driver.quit()
