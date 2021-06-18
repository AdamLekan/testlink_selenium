import unittest
from selenium import webdriver


class PriceTests(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('https://sklep.sizeer.com/puma-cruise-rider-wns-damskie-sneakersy-bialy-37486501')

    def test_new_price(self):
        # get the search textbox
        price= self.driver.find_element_by_class_name('b-productData')
        newPrice = price.find_element_by_class_name('s-newPrice')

        file = open("new_price.txt", "w", encoding='utf-8')
        file.write(newPrice.text)
        file.close()

        file = open("old_price.txt", "r", encoding='utf-8')
        oldPrice = file.read()
        file.close()

        file = open("new_price.txt", "r", encoding='utf-8')
        newPrice = file.read()
        file.close()
        print(newPrice)


        if oldPrice == newPrice:
            print('Cena nie została zmieniona')
        else:
            print('Cena została zmieniona')

        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)