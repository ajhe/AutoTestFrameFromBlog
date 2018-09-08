# coding=utf-8

from framework.base_page import BasePage

class HomePage(BasePage):

    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_input_box(self, text):
        self.type(self.input_box, text)

    def click_search_submit_btn(self):
        self.click(self.search_submit_btn)