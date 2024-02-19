# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s =Service("C:/Users/91979/OneDrive/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.get('https://google.com')
time.sleep(2)


#fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
user_input.send_keys('campusx')
time.sleep(1)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()

time.sleep(1)

link2 = driver.find_element(by=By.XPATH, value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
link2.click()
# Keep the browser window open until user presses Enter
input("Press Enter to close the browser...")
driver.quit()



