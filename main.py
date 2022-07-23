from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
import time

MY_PHONE_NUM = os.getenv("MY_PHONE_NUM")
LINK = "https://tinder.com/app/recs"

ser = Service(r"C:\Users\Sean\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get(LINK)
driver.implicitly_wait(25)
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_button.click()
time.sleep(1)
login_by_phone_number = driver.find_element(By.XPATH, '//*[@id="s369355022"]/div/div/div[1]/div/div/div[3]/span/div[3]/button')
login_by_phone_number.click()
phone_number = driver.find_element(By.XPATH, '//*[@id="s369355022"]/div/div/div[1]/div/div[2]/div/input')
phone_number.send_keys(f'{MY_PHONE_NUM}{Keys.ENTER}')
code = input("Press ENTER when you are ready to continue?: ")

allow_locations = driver.find_element(By.XPATH, '//*[@id="s369355022"]/div/div/div/div/div[3]/button[1]')
allow_locations.click()

enable_notifications = driver.find_element(By.XPATH, '//*[@id="s369355022"]/div/div/div/div/div[3]/button[1]')
enable_notifications.click()

privacy = driver.find_element(By.XPATH, '//*[@id="s2097736098"]/div/div[2]/div/div/div[1]/div[1]/button')
privacy.click()

like = driver.find_element(By.XPATH, '//*[@id="s2097736098"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
still_have_likes = True
while still_have_likes:
    time.sleep(1)
    clicked = False
    while not clicked:
        try:
            like.click()
            clicked = True
        except ElementClickInterceptedException:
            try:
                #if a match pops up it must be dismissed
                popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
                popup.click()
            except NoSuchElementException:
                try:
                    get_tinder_plus = driver.find_element((By.XPATH, '//*[@id="s369355022"]/div/div/div[3]/button[2]'))
                except NoSuchElementException:
                    #if a match fails to load
                    time.sleep(2)
