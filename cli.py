'''
@Copyright (c) 2019, Ryo Currency Project
@Author Max Base, Asrez Team
@Version 1.0
@Date 2019-11-02

Please see LICENSE for details
All rights reserved.
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import enum

class State(enum.Enum):
	NOBROWSER = 0
	LOGGEDIN = 1
	LOGGEDOUT = 2

# default setting
state=State.NOBROWSER

def browser():
	global browser
	global state
	print("[LOG] Open Browser")
	browser = webdriver.Firefox()
	state=State.LOGGEDOUT

def logout():
	global state
	print("[LOG] Logout")
	try:
		browser.get('https://twitter.com/logout')
		button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]')
		button.click()
	except:
		print("[ERR] Browser problem!")
		state=State.NOBROWSER

def login():
	global state
	print("[LOG] Login")
	try:
		browser.get('https://twitter.com/login?lang=en-gb')

		username = "AsrezCo"
		password = "Dd4fg56d12x3cve45g6f"

		username_box = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
		password_box = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
		button = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')

		if username_box and password_box and button:
			# username_box.send_keys(username + Keys.RETURN)
			username_box.send_keys(username)
			# password_box.send_keys(password + Keys.RETURN)
			password_box.send_keys(password)
			button.click()
			# Need to check you are loginned or not!
			# auth()
			state=State.LOGGEDIN
			'''
			verify_box = browser.find_element_by_xpath('//*[@id="challenge_response"]')
			if verify_box:
				# py 3 or 2.7?
				verify = input("Enter SMS Code: ")
				print(verify)
				verify_box.send_keys(verify)
			'''

			'''
			try:
				verify_box = WebDriverWait(driver, 20).until(
					browser.presence_of_element_located((By.XPATH, '//*[@id="challenge_response"]'))
				)
			finally:
				if verify_box:
					# py 3 or 2.7?
					verify = input("Enter SMS Code: ")
					print(verify)
					verify_box.send_keys(verify)
			'''

			# browser.quit()
		else:
			print("We have problem to detect login page!")
	except:
		print("[ERR] Browser problem!")
		state=State.NOBROWSER

def process():
	return

isProcess=False
while True:
	if state == State.NOBROWSER:
		isProcess=False
		browser()
	elif state == State.LOGGEDOUT:
		isProcess=False
		login()
	elif state == State.LOGGEDIN:
		if isProcess == False:
			isProcess=True
			print("[LOG] Process Twitter")
		process()
	# command=input("> ")
	# print(command)
	# if command == "login":
	# 	login()
	# elif command == "logout":
	# 	logout()
	# else:
	# 	print("Error!")
