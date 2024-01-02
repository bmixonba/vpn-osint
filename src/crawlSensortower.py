#!/bin/bash

from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the Selenium driver
options = webdriver.ChromeOptions()
options.add_argument("--headless") # run Chrome in headless mode to avoid opening a browser window
driver = webdriver.Chrome(options=options)

# Navigate to the SensorTower website and search for VPN applications
search_term = "vpn"
url = f"https://sensortower.com/ios/rankings/top/iphone/us/all-categories?date=2022-04-12&search={search_term}"
driver.get(url)

# Wait for the page to load and retrieve the HTML
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Find all the VPN applications on the page
vpn_apps = []
app_list = soup.find("ul", class_="table__body")
for app_item in app_list.find_all("li"):
    app_name = app_item.find("a", class_="app-info__name").text
    if "VPN" in app_name:
        vpn_apps.append(app_name)

# Print the list of VPN applications
print(vpn_apps)

# Clean up and close the Selenium driver
driver.quit()

