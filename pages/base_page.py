from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def find(self, locator, timeout=5):
        return WebDriverWait(
            self.driver, timeout,
            ignored_exceptions=[StaleElementReferenceException]).until(
            lambda d: d.find_element(*locator)
        )

    def click(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator, value):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_alert_text(self):
        alert = WebDriverWait(self.driver,timeout=5).until(
            EC.alert_is_present()
        )
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()