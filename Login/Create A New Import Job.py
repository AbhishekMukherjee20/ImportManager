from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get("https://bse-uk.tpointcloudplatform.com/BSETest/Login/?returnUrl=%2FBSETest%2Ftpointstudio%2Fstudio&loggedOff=True")
driver.maximize_window()
driver.find_element(By.ID, "UserName").click()
driver.find_element(By.ID, "UserName").click()
driver.find_element(By.ID, "UserName").send_keys("Sonali")
driver.find_element(By.ID, "Password").click()
driver.find_element(By.ID, "Password").send_keys("pass123#")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.get("https://bse-uk.tpointcloudplatform.com/BSETest/tpointstudio/Studio/application/Data")
driver.find_element(By.CSS_SELECTOR,"span[title='Imports']").click()
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, ".itemBox:nth-child(2) .lbl").click()
driver.find_element(By.CSS_SELECTOR, ".itemBox:nth-child(2) .clearfix:nth-child(3) .txt").click()
driver.switch_to.frame(0)
element = driver.find_element(By.ID, "ddlPackages")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.ID, "ddlPackages")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "ddlPackages").click()
dropdown =driver.find_element(By.ID, "ddlPackages")
dropdown = driver.find_element(By.CLASS_NAME,"txtdata").send_keys("abhidemo")
driver.find_element(By.ID, "fileSource").click()
driver.find_element(By.ID, "fileSource").send_keys("D:\\Office\\import1.csv")
driver.find_element(By.ID, "lbtFinish").click()
element =driver.find_element(By.ID, "df_frm547__RALG_ctlStatus")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.CSS_SELECTOR, ".container-fluid:nth-child(6) > .elementOuterBox:nth-child(1) .frmcontrol")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()