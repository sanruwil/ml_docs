#https://www.renaultsf.mx/
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRenault():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    print(self.vars)
  
  def teardown_method(self):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_renault(self):
    # Test name: renault
    # Step # | name | target | value
    # 1 | open | https://www.renaultsf.mx/ | 
    self.driver.get("https://www.renaultsf.mx/")
    # 2 | setWindowSize | 1301x816 | 
    self.driver.set_window_size(1301, 816)
    # 3 | click | css=.uppercase | 
    self.vars["window_handles"] = self.driver.window_handles
    # 4 | selectWindow | handle=${win5790} | 
    self.driver.find_element(By.CSS_SELECTOR, ".uppercase").click()
    # 5 | click | id=ContentPlaceHolder1_txtUsuario | 
    self.vars["win5790"] = self.wait_for_window(2000)
    # 6 | click | id=ContentPlaceHolder1_txtUsuario | 
    self.driver.switch_to.window(self.vars["win5790"])
    # 7 | type | id=ContentPlaceHolder1_txtUsuario | 1234566
    self.driver.find_element(By.ID, "ContentPlaceHolder1_txtUsuario").click()
    # 8 | click | id=ContentPlaceHolder1_txtPassword | 
    self.driver.find_element(By.ID, "ContentPlaceHolder1_txtUsuario").click()
    # 9 | type | id=ContentPlaceHolder1_txtPassword | 123456
    self.driver.find_element(By.ID, "ContentPlaceHolder1_txtUsuario").send_keys("1234566")
    # 10 | click | css=#ContentPlaceHolder1_Entrar > strong | 
    self.driver.find_element(By.ID, "ContentPlaceHolder1_txtPassword").click()
    # 11 | click | css=html | 
    self.driver.find_element(By.ID, "ContentPlaceHolder1_txtPassword").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_Entrar > strong").click()
    print(self.vars)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
 

myc=TestRenault()
myc.setup_method()
myc.test_renault()
myc.teardown_method()