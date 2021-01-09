from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTR_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
    CHECK = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2)")
    THIS = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    
