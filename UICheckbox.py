from selenium.webdriver.support import expected_conditions as ec
from UIElement import UIElement as Element

# Exercise #2
#
# Create Radiobutton/Checkbox class that will be inherited from UIElement class and will have a method
# to select the radio button/checkbox if it's not selected.


class UICheckbox(Element):
    """
    This class is for a checkbox element on the page, takes as parameters browser, method of locating element
    and locator itself
    """
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def click_checkbox(self):
        """
        Checks if element not selected yet and clicks on it
        """
        element = self.get_element()
        if not element.is_selected():
            element.click()
