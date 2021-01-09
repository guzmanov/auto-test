from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def check_url(self):
        assert "promo" in self.browser.current_url, ("Bad login url")

    def add_to_basket(self):
        element = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        element.click()

    def check_massege(self):
        element = self.browser.find_element(*ProductPageLocators.CHECK)
        result = element.text
        assert "был добавлен в вашу корзину." in result

    def check_work(self):
        pass

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CHECK), \
        "Success message is presented, but should not be"

    def do_this(self):
        assert self.is_disappeared(*ProductPageLocators.THIS), \
        "one two three four five"
