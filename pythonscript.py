# selenium for web driving
import selenium
from selenium import webdriver

# time for pausing between navigation
import time

# Datetime for recording time of submission
import datetime

# os for file management
import os


def print_off_localhost_info():
	driver = webdriver.Chrome()
	time.sleep(3)
	driver.get('http://localhost:3000/')
	time.sleep(4)
	id_box = driver.find_element_by_id("textBox")
	id_box.send_keys('lexiBoobz123')
	qr_sub = driver.find_element_by_id("submitQR")
	qr_sub.click()
	qr_sub.send_keys("/Users/jkoffman/Desktop/testFolderJasonApp/tempFolder/E40M HW1 copy/E40M\ HW1\ copy.png")
	time.sleep(10)

def log_into_drive():
	driver = webdriver.Chrome()
	time.sleep(1)
	driver.get('https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fmy-drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
	time.sleep(1)
	#proceed past username page
	#TO DO: if 2FA is enabled, this will be blocked!!!!!
	username_login_box = driver.find_element_by_id("identifierId")
	username_login_box.send_keys('jasonapp152@gmail.com')
	next_button = driver.find_element_by_id("identifierNext")
	next_button.click()
	time.sleep(2) # allows password page to populate before next find element call


	# proceed past login page
	pwd_login_box = driver.find_element_by_name("password")
	pwd_login_box.send_keys('1q2w3#4r%t')
	next_button = driver.find_element_by_id("passwordNext")
	next_button.click()

	#TO DO: there may be another page of stuff to skip. if so, we need some try, catch statements
	time.sleep(1000)












def submit_assignment(file_tup):
	# Using Chrome to access web
	driver = webdriver.Chrome()

	time.sleep(5)

	# Open the website
	driver.get('https://canvas.case.edu')

	# Password for Canvas
	with open('C:/Users/Will Koehrsen/Desktop/cp.txt', 'r') as f:
	    cp = f.read()


	# Locate id and password
	id_box = driver.find_element_by_name('username')
	pass_box = driver.find_element_by_name('password')

	# Send login information
	id_box.send_keys('wjk68')
	pass_box.send_keys(cp)

	# Click login
	login_button = driver.find_element_by_name('submit')
	login_button.click()

	# Find and click on list of courses
	courses_button = driver.find_element_by_id('global_nav_courses_link')
	courses_button.click()


	# Wait for the page to load
	time.sleep(2)

	# Get the name of the folder
	folder = file_tup[0]

	# Class to select depends on folder
	if folder == 'DSCI451':
	    class_select = driver.find_element_by_link_text('Applied Data Science Research (100/5047)')
	elif folder == 'DCSI453':
	    class_select = driver.find_element_by_link_text('Data Science: Statistical Learning, Modeling and Prediction (100/5046)')
	elif folder == 'EECS491':
	    class_select = driver.find_element_by_link_text('Artificial Intelligence: Probabilistic Graphical Models (100/10039)')
	elif folder == 'EECS531':
	    class_select = driver.find_element_by_link_text('Computer Vision (100/10040)')

	# Click on the specific class
	class_select.click()

	assignment_button = driver.find_element_by_link_text('Assignments')
	assignment_button.click()

	# Wait for the page to load
	time.sleep(2)

	# Locate the specific assignment
	file_name = file_tup[1]
	file_locator = file_name.split('.')[0]

	specific_assigment = driver.find_element_by_link_text(file_locator)
	specific_assigment.click()

	# Click on the button to submit an assignment
	try:
	    submit_assignment_button = driver.find_element_by_link_text('Submit Assignment')
	# If assignment has already been submitted
	except:
	    print('Assignment already submitted, re-submitting')
	    submit_assignment_button = driver.find_element_by_link_text('Re-submit Assignment')

	submit_assignment_button.click()

	# Wait for the page to load
	time.sleep(2)

	# Choose file button
	choose_file = driver.find_element_by_name('attachments[0][uploaded_data]')

	# Send the name of the file to the button
	file_location = os.path.join(submission_dir, folder, file_name)
	choose_file.send_keys(file_location)

	submit_assignment = driver.find_element_by_id('submit_file_button')
	submit_assignment.click()

	# Wait for the page
	time.sleep(2)

	# Move the file to the submitted folder
	submitted_dir = 'C:/Users/Will Koehrsen/Desktop/submitted_assignments'
	submitted_dir = os.path.join(submitted_dir, folder)
	submitted_file_name = 'Submitted ' + file_name

	submitted_file_location = os.path.join(submitted_dir, submitted_file_name)
	# os.rename(file_location, submitted_file_location)

	print('{} Assignment for Class {} successfully submitted at {}.'.format(
		file_name, folder, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

	print('Submitted assignment available at {}.'.format(submitted_file_location))

	return

if __name__ == "__main__":
	log_into_drive()
	# Build tuple of (folder, file) to turn in
	#submission_dir = 'C:/Users/Will Koehrsen/Desktop/completed_assignments'
	#dir_list = list(os.listdir(submission_dir))

	# for directory in dir_list:
	#     file_list = list(os.listdir(os.path.join(submission_dir, directory)))
	#     if len(file_list) != 0:
	#         file_tup = (directory, file_list[0])

	# if len(file_tup) == 0:
	# 	print('No files to submit')

	# else:
	# 	# print('Assignment "{}" for "{}" found.'.format(file_tup[1], file_tup[0]))
	# 	# input('Press enter to proceed: ')
	# 	submit_assignment(file_tup)
