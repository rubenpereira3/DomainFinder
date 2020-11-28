from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bird_api import get_bird_names
from menu import print_menu
import random


def get_bird_name():
	n = random.randint(0, len(bird_list) - 1)
	return bird_list[n]


bird_list = get_bird_names()

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

elem_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/span[1]"

while True:
	print("######################")
	print("##   Searching...   ##")
	print("######################")

	domain = get_bird_name() + ".info"
	url = f"https://pt.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={domain}"
	
	try:
		driver.get(url)
		wait = WebDriverWait(driver, 3)

		element_txt = wait.until(EC.presence_of_element_located((By.XPATH, elem_xpath))).text
	except:
		print("Element not found!")
		continue

	print("State: " + element_txt)
	available = element_txt.split(' ')[-1]
	
	if available == "disponível" or available == "Premium":
		print(domain + " está disponível!")
		print_menu()

		user_input = input(": ")
		while True:
			try:
				user_input = int(user_input)
				break
			except:
				user_input = input(": ")

		if user_input == 1:
			browser = webdriver.Chrome()
			browser.get(url)
			break
		if user_input == 2:
			continue
		if user_input == 3:
			driver.close()
			exit()
	
	else:
		print(domain + " já foi adquirido!")	
