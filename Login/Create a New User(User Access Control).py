from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get("https://bse-uk.tpointcloudplatform.com/BSETest/Login/?returnUrl=%2FBSETest%2Ftpointstudio%2Fstudio&loggedOff=True")
driver.maximize_window()
driver.find_element(By.ID, "UserName").click()
driver.find_element(By.ID, "UserName").send_keys("abhi20")
driver.find_element(By.ID, "Password").click()
driver.find_element(By.ID, "Password").send_keys("pass123#")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.get("https://bse-uk.tpointcloudplatform.com/BSETest/tpointstudio/Studio/application/Users")
driver.implicitly_wait(400)
driver.find_element(By.CSS_SELECTOR,"span[title='User Lists']").click()

driver.find_element(By.CSS_SELECTOR,"li[title='All Users'] span[class='pull-left txt']").click()
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[1]"))
driver.find_element(By.XPATH,"//span[normalize-space()='New']").click()
driver.find_element(By.XPATH,"//span[contains(@class,'filter-option pull-left')][normalize-space()='Select User Type']").click()
driver.find_element(By.XPATH,"//span[contains(@class,'text')][normalize-space()='Employee']").click()
driver.find_element(By.XPATH,"//span[contains(@class,'filter-option pull-left')][normalize-space()='Select Security Profile']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Low']").click()
driver.find_element(By.CLASS_NAME,"frmtxtdatareq").click()
driver.find_element(By.CLASS_NAME,"frmtxtdatareq").send_keys("qat")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]/div[1]/input[1]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/input[1]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("team")


driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[4]/div[1]/div[1]/input[1]").click()
driver.find_element(By.CSS_SELECTOR,".ui-datepicker-month").click()
driver.find_element(By.CSS_SELECTOR,".ui-datepicker-month").send_keys("October")
driver.find_element(By.CSS_SELECTOR,".ui-datepicker-year").click()
driver.find_element(By.CSS_SELECTOR,".ui-datepicker-year").send_keys("2021")
driver.find_element(By.XPATH,"//button[normalize-space()='Done']").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/input[1]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/input[1]").send_keys("qteam")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/input[1]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/input[1]").send_keys("pass123#")


driver.find_element(By.XPATH,"//span[@class='lbl pull-left'][normalize-space()='Save']").click()

