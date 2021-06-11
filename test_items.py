link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_btn(browser):
    browser.get(link)
    add_btn = len(browser.find_elements_by_css_selector("button[class='btn btn-lg btn-primary btn-add-to-basket']"))
    assert add_btn > 0, "no such element"
