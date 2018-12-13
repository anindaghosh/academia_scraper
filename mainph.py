from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import yaml

login_url = "https://academia.srmuniv.ac.in/"
after_login = "https://academia.srmuniv.ac.in/#View:My_Attendance"
subject_list = []
attendance_list = []
hours_conducted = []
hours_absent = []

driver = webdriver.PhantomJS()
driver.get(login_url)
driver.switch_to_frame("zohoiam")

with open("login.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# Typing the details

usertext = driver.find_element_by_xpath("//input[@name = 'username']")
usertext.send_keys(cfg['login']['username'])
passtext = driver.find_element_by_xpath("//input[@name = 'password']")
passtext.send_keys(cfg['login']['password'])

# Submitting the form

submit_button = driver.find_element_by_xpath("//input[@value = 'Sign In']")
submit_button.submit()

# Go to attendance

time.sleep(6)
print("Logged in!")
driver.get(after_login)
time.sleep(3)

# Getting data

for i in range(2,12):
	sub = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[2]")
	att = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[9]")
	hc = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[7]")
	ha = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[8]")
	subject_list.append(sub.text)
	attendance_list.append(att.text)
	hours_conducted.append(hc.text)
	hours_absent.append(ha.text)

print("Your attendance is as follows:\n")
for i in range(10):
	print(str(i+1) + ". " + str(subject_list[i]) + " - " + str(attendance_list[i]) + "%")

print("\nNo. of classes you can safely bunk:\n")

for i in range(10):
	perc = 1 - (int(hours_absent[i])/int(hours_conducted[i]))
	print(perc)
	# while perc>=75:
