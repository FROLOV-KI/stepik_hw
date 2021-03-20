import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_present_on_page(browser):
    browser.get(link)
    time.sleep(30)
    try:
        add_button = browser.find_element_by_class_name("btn-add-to-basket")
        check = True
    except:
        check = False
    assert check, "КНОПКА НЕ НАЙДЕНА!"
    
        
