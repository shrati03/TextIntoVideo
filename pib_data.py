from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd

def create_webdriver(browser):
    if browser == 'chrome':
        # Specify the path to the ChromeDriver executable
        return webdriver.Chrome()
    elif browser == 'firefox':
        # Specify the path to the GeckoDriver (Firefox) executable
        return webdriver.Firefox()
    elif browser == 'edge':
        # Specify the path to the Edge WebDriver executable
        # edge_driver_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Replace with the actual path to your Edge WebDriver executable
        return webdriver.Edge()
    # Add support for other browsers as needed
    else:
        raise ValueError("Unsupported browser")

# Choose the browser you want to use
selected_browser = 'edge'  # Change this to 'firefox', 'edge', or any other supported browser

# Initialize the WebDriver based on the selected browser
driver = create_webdriver(selected_browser)

# Define the URL of the webpage you want to scrape
url = "https://www.pib.gov.in/PressReleasePage.aspx?PRID=1954558"  # Replace with your desired URL

# Send an HTTP GET request to the URL
driver.get(url)

# Wait for the page to load (you may need to adjust the sleep time)
import time
time.sleep(5)

# Get the page source after waiting
page_source = driver.page_source

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(page_source, "html.parser")

# Find and extract data using BeautifulSoup
# Replace the following lines with your specific scraping logic
paragraph_elements = soup.find_all("p")
paragraph_text = [p.text.strip() if paragraph_elements else "N/A" for p in paragraph_elements]

# Create a DataFrame to store the data
df = pd.DataFrame(paragraph_text, columns=['Paragraph'])
df.to_csv('./scraped_data.csv', index=False)

# Save the data to a csv file
print("Data saved to 'scraped_data.csv'")

# Close the WebDriver
driver.quit()
