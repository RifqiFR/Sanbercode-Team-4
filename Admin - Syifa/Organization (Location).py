import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Organization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_add_location_success(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # Open Website
        time.sleep(3)
        # Login
        driver.find_element(By.NAME, "username").send_keys("Admin") # Input Username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # Input Password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "oxd-button").click() # Click Login
        time.sleep(3)
        # Change to Page Location
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() # Click Admin Menu
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() # Click Sub Menu Organization
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() # Click Location
        time.sleep(2)
        # Add Location
        driver.find_element(By.XPATH, "//div[@class='orangehrm-header-container']/div[1]/button").click() # Click Add
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[1]/div/div/div/div[2]/input").send_keys("Jessica") # Input Name
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[1]/div/div[2]/input").send_keys("Bandung") # Input City
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[4]/div/div[2]/div/div").click() # Click Drop Down
        time.sleep(5)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[4]/div/div[2]/div/div[2]/div[101]").click() # Click Indonesia
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[3]/button[2]").click() # Click Save
        time.sleep(5)

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_add_location_failed(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # Open Website
        time.sleep(3)
         # Login
        driver.find_element(By.NAME, "username").send_keys("Admin") # Input Username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # Input Password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "oxd-button").click() # Click Login
        time.sleep(3)
        # Change to Page Location
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() # Click Admin Menu
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() # Click Sub Menu Organization
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() # Click Location
        time.sleep(2)
        # Add Location
        driver.find_element(By.XPATH, "//div[@class='orangehrm-header-container']/div[1]/button").click() # Click Add
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[1]/div/div/div/div[2]/input").send_keys("Jessica") # Input Name
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[1]/div/div[2]/input").send_keys("Bandung") # Input City
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[3]/button[2]").click() # Click Save
        time.sleep(5)

        #validationn
        response_message = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/span").text

        self.assertEqual('Required', response_message)
    
    def test_edit_location_success(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # Open Website
        time.sleep(3)
        # Login
        driver.find_element(By.NAME, "username").send_keys("Admin") # Input Username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # Input Password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "oxd-button").click() # Click Login
        time.sleep(3)
        # Change to Page Location
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() # Click Admin Menu
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() # Click Sub Menu Organization
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() # Click Location
        time.sleep(2)
        # Edit Location
        driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[3]/div/div[7]/div/button[2]").click() # Click Pen Button (Jessica)
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div/div/div[2]/input").send_keys(Keys.CONTROL,"a")
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div/div/div[2]/input").send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div/div/div[2]/input").send_keys("Jakarta") # Change into Jakarta
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[3]/button[2]").click() # Click Save
        time.sleep(2)

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_delete_location_success(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # Open Website
        time.sleep(3)
        # Login
        driver.find_element(By.NAME, "username").send_keys("Admin") # Input Username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # Input Password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "oxd-button").click() # Click Login
        time.sleep(3)
        # Change to Page Location
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() # Click Admin Menu
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() # Click Sub Menu Organization
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() # Click Location
        time.sleep(2)
        # Delete Location
        driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[3]/div/div[7]/div/button[1]").click() # Click Button Delete (Jessica)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]").click() # Delete Confirmation
        time.sleep(2)

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

if __name__ == "__main__": 
    unittest.main()