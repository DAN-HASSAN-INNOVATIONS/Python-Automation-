# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# define url
# FILL IN
url = "FILL IN"

# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage 
driver.get(url)

# define a wait
# uncomment the following line and write your code
# wait = 

# find the Enable button
enable_button = driver.find_element(By.XPATH, 'FILL IN')
# click the Enable button
enable_button.click()
sleep(3)

# find the disable button
# uncomment the following line and FILL IN 
# disable_button = wait.until(EC.element_to_be_clickable((By.XPATH, 'FILL IN')))
# click the Disable button
# disable_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the Remove button
# FILL IN
remove_button = driver.find_element(By.XPATH, 'FILL IN')
# click the Remove button
remove_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the Add button
# uncomment the following line and FILL IN
# add_button = wait.until(EC.element_to_be_clickable((By.XPATH, 'FILL IN')))
# click the Add button
# add_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the checkbox 
# uncomment the following line and FILL IN
# checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, 'FILL IN')))
# click the checkbox
# checkbox.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# close the browser and quit the webdriver
driver.quit()