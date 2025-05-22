from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张三听说有一个在线待办事项的应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到网页标题和主标题都包含“To-Do”这两个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text  # (#1)
        self.assertIn('To-Do', header_text)

        # 应用有一个输入框，可以输入待办事项
        inputbox = self.browser.find_element(By.ID, 'id_new_item')  # (#2)
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 他在文本框中输入了“Buy flowers”
        inputbox.send_keys('Buy flowers')  # (#2)
        
        # 他按下回车键，页面更新了
        self.browser.find_element(By.ID, 'id_list_table')  # (#1)
        inputbox.send_keys(Keys.ENTER)  # (#3)
        time.sleep(1)  # (#4)

        # 页面中显示了他输入的“1: Buy flowers”
        table = self.browser.find_element(By.ID, 'id_list_table')  # (#1)
        rows = table.find_elements(By.TAG_NAME, 'tr')  # (#1)
        self.assertIn('1: Buy flowers', [row.text for row in rows])  # (#1)

        # 页面中显示了一个文本输入框，可以输入其他待办事项
        # 他输入了“gift to girlfriend”
        inputbox = self.browser.find_element(By.ID, 'id_new_item')  # (#2)
        inputbox.send_keys('gift to girlfriend')  # (#2)

        # 页面更新后，列表中显示了这两个待办事项
        self.fail('Finish the test!')  # 还需要添加更多验证事项

if __name__ == '__main__':  # (#6)
    unittest.main()