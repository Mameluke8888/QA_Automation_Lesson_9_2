from UIElement import UIElement as Element
from selenium.webdriver.support.select import Select

# Exercise #1
#
# Update Dropdown class with deselect methods


class Dropdown(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def select_by_text(self, option):
        """
        Selects the option in dropdown by visible text
        :param option: option to select
        """
        Select(self.get_element()).select_by_visible_text(option)

    def select_by_value(self, value):
        """
        Selects the option in dropdown by value attribute
        :param value: value attribute
        """
        Select(self.get_element()).select_by_value(value)

    def select_by_index(self, index):
        """
        Selects the option in dropdown by index
        :param index: index of the option
        """
        Select(self.get_element()).select_by_index(index)

    def deselect_by_text(self, option):
        """
        Deselects the option in dropdown by visible text
        :param option: option to select
        """
        Select(self.get_element()).deselect_by_visible_text(option)

    def deselect_by_value(self, value):
        """
        Deselects the option in dropdown by value attribute
        :param value: value attribute
        """
        Select(self.get_element()).deselect_by_value(value)

    def deselect_by_index(self, index):
        """
        Deselects the option in dropdown by index
        :param index: index of the option
        """
        Select(self.get_element()).deselect_by_index(index)

    def deselect_all(self):
        """
        Deselects all of the options in dropdown
        """
        Select(self.get_element()).deselect_all()
