#Locating Web Elements - Program Notes Download

from selenium import webdriver

#open the browser
driver= webdriver.Firefox()
#navigate to the URL
driver.get("http://facebook.com")

#Locate the web element by attribute 'name' and then Input the data
driver.find_element_by_name("firstname").send_keys("Joby")

#Locate the web element by attribute 'id' and then Input the data
driver.find_element_by_id("u_0_3").send_keys("Joseph")

#Locate the web element by attribute 'class name' and then Input the data
driver.find_element_by_class_name("inputtext").send_keys("test@selenium.com")

#Locate the web element by attribute 'id' and then invoke the click button.
#driver.find_element_by_id("u_0_i").click()

#Locate the web element by 'link_text' and then click on the link.
driver.find_element_by_link_text("Forgot your password?").click()

#Locate the web element by 'partial link_text' and then click on the link.
#driver.find_element_by_partial_link_text("Forgot your")