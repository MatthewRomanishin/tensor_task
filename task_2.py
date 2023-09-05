from page_objects.YandexPages import SearchHelper
import pytest
from selenium import webdriver
import time


# @pytest.fixture(scope="session")
def test():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()

    yandex_main_page = SearchHelper(driver)
    yandex_main_page.go_to_site()
    time.sleep(1)
    yandex_main_page.click_on_the_search_field()
    time.sleep(1)

    menu_button = yandex_main_page.find_menu_button()
    assert menu_button != None
    yandex_main_page.click_on_the_menu_button()
    time.sleep(1)

    yandex_main_page.click_on_the_picture_button()
    time.sleep(1)
    yandex_main_page.switch_to_last_page()
    current_url = yandex_main_page.current_url()
    assert current_url == "https://ya.ru/images/"

    yandex_main_page.click_on_the_popular_picture_button()
    yandex_main_page.switch_to_last_page()
    time.sleep(2)

    input_ = yandex_main_page.check_input_field()
    assert input_ != ""
    time.sleep(2)

    base_url = yandex_main_page.current_url()
    yandex_main_page.click_on_the_first_picture()
    time.sleep(3)
    yandex_main_page.switch_to_last_page()
    first_picture_url = yandex_main_page.current_url()
    first_picture_src = yandex_main_page.get_image_src()
    assert base_url != first_picture_url

    yandex_main_page.click_on_the_next_button()
    time.sleep(2)
    yandex_main_page.switch_to_last_page()
    second_picture_src = yandex_main_page.get_image_src() 
    assert first_picture_src != second_picture_src

    yandex_main_page.click_on_the_previous_button()
    yandex_main_page.switch_to_last_page()
    current_picture_src = yandex_main_page.get_image_src()
    assert first_picture_src == current_picture_src

    print("Done!")

if __name__ == '__main__':
    test()