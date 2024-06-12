import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import schedule

# Function to open a website
def open_website():
    # Set up the WebDriver (Chrome in this case)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    url = "https://www.gartner.com"  # Replace with your target URL
    driver.get(url)
    print(f"Opened {url} at {datetime.now()}")
    # Optional: Add any other actions you want to perform on the website here
    # driver.quit()  # Uncomment this line to close the browser after opening the website

# Schedule the task to run at a specific time
def schedule_task():
    schedule_time = "16:30"  # 24-hour format (e.g., 3:30 PM)
    schedule.every().day.at(schedule_time).do(open_website)

    while True:
        schedule.run_pending()
        time.sleep(100)

if __name__ == "__main__":
    schedule_task()
