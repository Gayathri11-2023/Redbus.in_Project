from selenium.webdriver.common.by import By
class WebLocator:
    def __init__(self):
        self.fromInput_Locator = "//*[@id='src']"
        self.toInput_Locator = "//*[@id='dest']"
        self.busSearch_button_Locator = "//*[@id='search_button']"
        self.date_picker = '//*[@id="onwardCal"]/div/div/span'
        self.choosen_date ='//*[@id="onwardCal"]/div/div[2]/div/div/div[3]/div[3]/span/div[2]/span'
        self.train_ticket_locator = '//*[@id="rail_tickets_vertical"]'
        self.from_Locator_Train = '//*[@id="root"]/section/div/div[3]/div[2]/div/form/div[1]/label'
        self.fromInput_Locator_Train ='//*[@id="root"]/section/div/div[3]/div[2]/div/div/div/div/div[2]'
        self.toLocator_Train = '//*[@id="root"]/section/div/div[3]/div[2]/div/form/div[2]/label'
        self.toInput_locator_Train = '//*[@id="root"]/section/div/div[3]/div[2]/div/div/div/div/div[3]'
        self.date_picker_train = '//div[@class="home_calendar"]'
        self.choosen_date_train ='//*[@id="root"]/section/div/div[3]/div[2]/div/div/div/div/div[3]/span[3]/div[6]/span'
        self.checkbox_locator = '//*[@id="root"]/section/div/div[3]/div[2]/div/form/div[4]/div[2]'
        self.search_trains_locator = '//*[@id="root"]/section/div/div[3]/div[2]/div/form/button'
    def entertext(self, driver, locator, textvalue):
        driver.find_element(by=By.XPATH, value=locator).send_keys(textvalue)


    def buttonClick(self, driver, locator):
        driver.find_element(by=By.XPATH, value=locator).click()