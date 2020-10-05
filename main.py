from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
print("I am here")
driver.get("https://www.cricbuzz.com/live-cricket-scores/30409/rcb-vs-dc-19th-match-indian-premier-league-2020")

for i in range(5):
	print(driver.title)
	time.sleep(5)
