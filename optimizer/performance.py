import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def analyze_website(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Setup WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Start timing the page load
    start_time = time.time()
    driver.get(url)  # Load the website
    end_time = time.time()

    # Get performance metrics from the browser
    navigation_timing = driver.execute_script("return window.performance.timing")
    driver.quit()

    # Calculate key performance metrics
    page_load_time = (navigation_timing["loadEventEnd"] - navigation_timing["navigationStart"]) / 1000
    return round(page_load_time, 2)
