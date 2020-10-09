from selenium.webdriver.common.by import By

from hubspot.POM.Basepage import Basepage
from hubspot.POM.Password import Password
from hubspot.testdata.Testdata import Testdata


class Username(Basepage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.URI)

    email_field = (By.XPATH, "//input[@type='email']")
    continue_field = (By.XPATH, "//input[@id='continue']")
    need_help = (By.XPATH, "//span[contains(@class,'a-expander')]")
    create_acc = (By.XPATH, "//a[@id='createAccountSubmit']")
    warning = (By.XPATH,"//div[@class='a-box-inner a-alert-container']/div[contains(text(),'Enter')]")

    def eneter_Username(self, data):
        self.enter_values(self.email_field, data)

    def get_title_name(self):
        return self.get_title()

    def need_help_disp(self):
        if self.element_displayed(self.need_help):
            return self.link_is_present(self.need_help)

    def button_displayed(self):
        return self.element_displayed(self.create_acc)

    def cont_click(self):
        if self.element_displayed(self.continue_field):
            self.driver.find_element(*Username.continue_field).click()
            password = Password(self.driver)
            return password

    def warning_present(self):
        return self.link_is_present(self.warning)





