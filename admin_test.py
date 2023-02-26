import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())  

    def tearDown(self):
        self.driver.quit()

    def login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") #buka web
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") 
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)

    def job_title_page(self):
        driver = self.driver
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click()
        time.sleep(2)

    def test_add_job_title(self): 
        self.login()
        self.job_title_page()
        driver = self.driver

        # Add Job Title Page
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[1]/div/div[2]/input").send_keys("Back-End")
        time.sleep(3)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[5]/button[2]").click()
        time.sleep(10)

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_edit_job_title(self):

        self.login(driver)
        self.job_title_page(driver)
        driver = self.driver

        # Edit Job Title 
        driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[2]/div/div[4]/div/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[1]/div/div[2]/input").send_keys(Keys.CONTROL, 'a')
        time.sleep(3)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[1]/div/div[2]/input").send_keys(Keys.BACKSPACE)
        time.sleep(3)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[1]/div/div[2]/input").send_keys("Back-End Engineer")
        time.sleep(3)
        driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[5]/button[2]").click()
        time.sleep(10)

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_delete_job_title(self):

        self.login(driver)
        self.job_title_page(driver)
        driver = self.driver

        #Delete Job Title
        driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[2]/div/div[4]/div/button[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='orangehrm-modal-footer']/button[2]").click()
        time.sleep(5)

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

if __name__ == '__main__':
    unittest.main()
