from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

# imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# imports form internal modules
from browser import Browser
from UIElement import UIElement as Element
from dropdown import Dropdown
from UICheckbox import UICheckbox as Checkbox

import time

# Exercise #1
#
# Update Dropdown class with deselect methods

# Exercise #2
#
# Create Radiobutton/Checkbox class that will be inherited from UIElement class and will have a method
# to select the radio button/checkbox if it's not selected.

# May 14th, 2021
# student Evgeny Abdulin

browser = Browser("https://techskillacademy.net/brainbucket/index.php?route=account/login", "Firefox")
driver = browser.get_driver()

# sending a password to a login page
password_login_input = Element(browser, By.ID, "input-password")
password_login_input.enter_text("password")

# clicking a button to go to the registration page, waiting until clickable
new_registrant_btn = browser.get_wd_wait().until(ec.element_to_be_clickable((By.XPATH,
                                                                             "//a[contains(text(), 'Continue')]")))
new_registrant_btn.click()

# checking if title Register Account is visible
register_title = browser.get_wd_wait().until(ec.visibility_of_element_located((By.XPATH, "//h1")))


# filling fields/checking 'required' on the registration page
def filling_field(f_xpath, f_id, f_keys, assert_needed=False):
    if assert_needed:
        field = Element(browser, By.XPATH, f_xpath)
        field_class = field.get_attribute("class", False)
        assert "required" in field_class
    f_input = Element(browser, By.ID, f_id)
    f_input.enter_text(f_keys)


fields = [
    ("input-firstname", "//fieldset/div[2]", "Evgeny", True),
    ("input-lastname", "//fieldset/div[3]", "Abdulin", True),
    ("input-email", "//fieldset/div[4]", "abdulin.evgeny@gmail.com", True),
    ("input-telephone", "//fieldset/div[5]", "512-888-8888", True),
    ("input-fax", "", "512-999-9999", False),
    ("input-company", "", "Texas State University", False),
    ("input-address-1", "//fieldset[2]/div[2]", "601 University Drive", True),
    ("input-address-2", "", "Apt X", False),
    ("input-city", "//fieldset[2]/div[4]", "San Marcos", True),
    ("input-postcode", "", "78666-4684", False),
    ("input-password", "//fieldset[3]/div[1]", "superpassword", True),
    ("input-confirm", "//fieldset[3]/div[2]", "superpassword", True)]

for f in fields:
    filling_field(f[1], f[0], f[2], f[3])

# selecting region/state
state_dropdown = Dropdown(browser, By.ID, "input-zone")
state_dropdown.select_by_text("Texas")

# agree to privacy policy
agree_btn = Checkbox(browser, By.XPATH, "//input[@name='agree']")
agree_btn.click_checkbox()

# NO to subscription
subscribe_btn = Checkbox(browser, By.XPATH, "//input[@name='newsletter' and @value='0']")
subscribe_btn.click_checkbox()

continue_btn = Element(browser, By.XPATH, "//input[@value='Continue']")

# getting the background color of Continue button
background_color = continue_btn.get_element().value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'

# add some sleep time to be able to see the result
time.sleep(5)

browser.shutdown()
