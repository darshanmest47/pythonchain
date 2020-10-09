import time

from selenium.webdriver.common.by import By

from hubspot.POM.Basepage import Basepage
from hubspot.testdata.Testdata import Testdata


class Password(Basepage):

    def __init__(self,driver):
        super().__init__(driver)
        # self.driver.get(Testdata.URI1)

    pass_field = (By.XPATH, "//input[@type='password']")
    chk_box = (By.XPATH, "//i[contains(@class,'icon-check')]")
    forgot_pass = (By.XPATH, "//a[@id='auth-fpp-link-bottom']")
    submit_btn = (By.XPATH, "//input[@id='signInSubmit']")
    email_veri = (By.XPATH, "//span[contains(text(),'suraj')]")
    warn_msg = (By.XPATH, "//div[contains(@class,'a-alert-container')]/div")

    def email_verify(self):
        email_text = self.link_is_present(self.email_veri)
        return email_text

    def forgot_passtext(self):
        pass_text = self.link_is_present(self.forgot_pass)
        return pass_text

    def checkbox_chk(self):
        if self.link_is_present(self.chk_box):
            self.perform_click(self.chk_box)

    def warn_verify(self):
        self.perform_click(self.submit_btn)

        wrn_txt=self.text_is_present(self.warn_msg)
        return wrn_txt

    def password_enter(self, val):
        self.enter_values(self.pass_field, val)

    def click_sub(self):
        if self.link_is_present(self.submit_btn):

            self.perform_click(self.submit_btn)




