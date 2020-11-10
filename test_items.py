import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    button = browser.find_element_by_id("add_to_basket_form")
    assert button is not None, 'The button is absent'

