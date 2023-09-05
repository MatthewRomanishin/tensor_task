import pytest
from selenium import webdriver
from page_objects.YandexPages import SearchHelper
import time

def test_search():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    yandex_main_page = SearchHelper(driver)
    yandex_main_page.go_to_site()

    search_field = yandex_main_page.find_search_field()
    assert search_field != None 

    yandex_main_page.enter_word('Тензор')
    time.sleep(2)

    suggests = yandex_main_page.find_suggests()
    assert len(suggests) != 0

    yandex_main_page.enter()

    time.sleep(2)

    results = yandex_main_page.find_results()
    assert len(results) != 0

    first_result_link = yandex_main_page.get_first_result_link()
    tensor_link = "https://tensor.ru/"

    assert first_result_link == tensor_link

    print("Done!")

if __name__ == '__main__':
    test_search()