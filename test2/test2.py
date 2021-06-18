import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('https://en.wikipedia.org/wiki/Barack_Obama')
        cls.driver.title

    def test_change_webside(self):
        # get the search textbox
        element = self.driver.find_element_by_tag_name('body')

        file = open("new_page.txt", "w", encoding='utf-8')
        file.write(element.text)
        file.close()

        file = open("old_page.txt", "r", encoding='utf-8')
        old = file.read()
        file.close()

        file = open("new_page.txt", "r", encoding='utf-8')
        new = file.read()
        file.close()

        if old == new:
            print('Strona nie została zmodyfikowana')
        else:
            print('Strona została zmodyfikowana')

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)