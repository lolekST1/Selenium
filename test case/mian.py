import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):        # wykonuje się przed każdym testem
        self.driver = webdriver.Chrome("D:\OneDrive\Elektronika\Programowanie\Testowanie\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_example(self):     # jak zaczynamy od prefixu test_ to będzie uruchomione
        print("Test")
        assert True         # jeśli prawda - test zdany

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):         # wykonuje się po kazdym teście
        self.driver.close()

if __name__ == "__main__":
    unittest.main()         # uruchamia wszystkie testy
