import pytest
#own packages
from Data import data1
from Locator import locator1

#common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
#action chains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

#Exceptions
from selenium.common.exceptions import NoSuchElementException

#sleep
from time import sleep

#explicitwait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random


class Test_Search:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome()

        #self.wait = WebDriverWait(self.driver, 10)
        #self.action = ActionChains(self.driver)
        yield
        self.driver.quit()


    def test_available_buses(self, boot):
         try:
            self.driver.get(data1.WebData().url)
            self.driver.maximize_window()
            sleep(5)
            #getting from  input from the user
            locator1.WebLocator().entertext(self.driver, locator1.WebLocator().fromInput_Locator, data1.WebData().fromInput)
            sleep(3)
            locator1.WebLocator().entertext(self.driver, locator1.WebLocator().toInput_Locator, data1.WebData().toInput)
            sleep(3)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().date_picker)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().choosen_date)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().busSearch_button_Locator)
            sleep(5)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().train_ticket_locator)
            sleep(5)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().from_Locator_Train)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().fromInput_Locator_Train)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().toLocator_Train)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().toInput_locator_Train)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().date_picker_train)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().choosen_date_train)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().checkbox_locator)
            sleep(2)
            locator1.WebLocator().buttonClick(self.driver, locator1.WebLocator().search_trains_locator)
            sleep(5)

         except NoSuchElementException as e:
             print("Error:Element is not present in the webpage")












