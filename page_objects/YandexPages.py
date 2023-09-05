from page_objects.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.XPATH, "/html/body/main/div[3]/form/div[2]/button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_MENU = (By.CLASS_NAME, "services-suggest__icons-more")
    LOCATOR_YANDEX_PICTURES = (By.XPATH, "/html/body/main/div[4]/div/div[1]/div/div[3]/div[1]/span[9]/a/div[1]")
    LOCATOR_POPULAR_PUCTURE_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Shadow")
    LOCATOR_FIRST_IMAGE = (By.CLASS_NAME, "serp-item__link")
    LOCATOR_NEXT_PREVIOUS_BUTTONS = (By.CLASS_NAME, "CircleButton-Icon")
    LOCATOR_IMAGE_LINK = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_SUGGESTS = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_SEARCH_RESULTS = (By.ID, "search-result")
    LOCATOR_FIRST_RESULT_LINK = (By.XPATH, "//*[@id='search-result']/li[1]/div/div[2]/div[1]/a")
                                            
class SearchHelper(BasePage):

    def switch_to_last_page(self):
        return BasePage.switch_to_last_page(self)

    def current_url(self):
        current_url = BasePage.current_url(self)
        return current_url
    
    def find_search_field(self):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=2)
        return search_field
    
    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=2)
        search_field.click()
        search_field.send_keys(word)
        return search_field
    
    def enter(self):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=2)
        return search_field.send_keys(Keys.ENTER)

    def find_results(self):
        return self.find_elements(YandexSeacrhLocators.LOCATOR_SEARCH_RESULTS, time=2)

    def find_suggests(self):
        suggests = self.find_elements(YandexSeacrhLocators.LOCATOR_SUGGESTS, time=2)
        return suggests

    def get_first_result_link(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_RESULT_LINK, time=2).get_attribute("href")
    
    def find_menu_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_MENU, time=2)
    
    def click_on_the_search_field(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=2).click()
    
    def click_on_the_menu_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_MENU, time=2).click()

    def click_on_the_picture_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURES, time=2).click()

    def click_on_the_popular_picture_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_POPULAR_PUCTURE_CATEGORY, time=2).click()

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_input_field(self):
        return self.find_element((By.NAME, "text"), time=2).get_attribute("value")

    def click_on_the_first_picture(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_IMAGE, time=2).click()

    def click_on_the_next_button(self):
        return self.find_elements(YandexSeacrhLocators.LOCATOR_NEXT_PREVIOUS_BUTTONS, time=2)[-1].click()

    def click_on_the_previous_button(self):
        return self.find_elements(YandexSeacrhLocators.LOCATOR_NEXT_PREVIOUS_BUTTONS, time=2)[0].click()

    def get_image_src(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_LINK).get_attribute("src")

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu