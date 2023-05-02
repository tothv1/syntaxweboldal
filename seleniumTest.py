from distutils.spawn import find_executable
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

bongeszo = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Oldal megnyitás
bongeszo.get('http://84.2.242.173:5500/noiruha.html')
bongeszo.maximize_window()
time.sleep(1)
bongeszo.save_screenshot('noiruha_megnyitas.png')

# női ruházat
vasarlas = bongeszo.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/button')
bongeszo.execute_script("arguments[0].scrollIntoView();", vasarlas)
time.sleep(1)

vasarlas.click()
time.sleep(1)

bongeszo.save_screenshot('kattint_pink_polo.png')
lol = bongeszo.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div/div[3]/button[1]')
lol.click()
time.sleep(1)

cipok = bongeszo.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/a[5]')
cipok.click()
time.sleep(1)

bongeszo.save_screenshot('cipok_oldal.png')
aaaaa = bongeszo.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/button')
bongeszo.execute_script("arguments[0].scrollIntoView();", aaaaa)
time.sleep(1)

aaaaa.click()
time.sleep(1)
bongeszo.save_screenshot('cipokep.png')

bongeszo.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div/div[3]/button[1]').click()
time.sleep(1)



bongeszo.close()