from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def enter_values(self, locator, data):
        ele = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        ele.send_keys(data)

    def link_is_present(self, locator):
        ele1 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        return ele1.text

    def get_title(self):
        title = self.driver.title
        return title

    def element_displayed(self, locator):
        ele2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).is_displayed()
        return bool(ele2)

    def perform_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def text_is_present(self,locator):
        ele1=WebDriverWait(self.driver , 30).until(EC.presence_of_element_located(locator))
        return ele1.text
