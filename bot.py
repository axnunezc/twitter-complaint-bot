from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_driver_path = "/Users/axel/Documents/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.up = 0
        self.down = 0
        
    def get_internet_speeds(self):
        # Open speedtest
        self.driver.get("https://www.speedtest.net/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "start-text")))
        
        # Start test
        start_btn = self.driver.find_element_by_class_name("js-start-test")
        start_btn.click()
    
        sleep(120)
        
        results = self.driver.find_elements_by_class_name("result-data-large")
            
        self.down = float(results[1].text)
        self.up = float(results[2].text)
        
        
    def twitter_login(self, email, username, password):
        # Open twitter
        self.driver.get("https://twitter.com/home")
        sleep(2)

        # Provide username
        email_input = self.driver.find_element_by_xpath("//input[@name='text']")
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        sleep(2)
        
        confirm_input = self.driver.find_element_by_xpath("//input[@name='text']")
        confirm_input.send_keys(username)
        confirm_input.send_keys(Keys.RETURN)
        sleep(2)
            
        # Provide password   
        password_input = self.driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
            
    
    def tweet_at_provider(self, expected_up, expected_down):
        sleep(2)
        
        # Get hold of tweet field
        tweet_field = self.driver.find_element_by_class_name("public-DraftStyleDefault-block")
        
        # Compose tweet
        tweet_field.send_keys(f"Hey ISP, why is my internet speed {self.down} down / {self.up} up when I pay for {expected_down} down / {expected_up} up?")
        
        # Tweet out
        self.driver.find_element_by_xpath("//div[@data-testid='tweetButtonInline']").click()
        