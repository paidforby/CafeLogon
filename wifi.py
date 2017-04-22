from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.example.com") #any http site will do

#Accept T&C checkbox
checkbox = driver.find_element_by_id("comcastTermsCondition") #yes, that is really the id of the checkbox
checkbox.click()

#driver.implicitly_wait(2)
sleep(5) #had difficulty with implicit wait with my firefox verision

#Click Connect button by submiting form it is contained within
form = driver.find_element_by_class_name("atn-button-text")
form.submit() #this currently opens a logout window? I don't mind it really, might be able to use it to do auto-reset?

driver.close()
