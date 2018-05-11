import pytest;

def test_title(setup_driver):
    setup_driver.get('http://lauriegreen.scot/')
    setup_driver.maximize_window()
    assert "Laurie Green" in setup_driver.title
    
def test_header(setup_driver):
    setup_driver.get('http://lauriegreen.scot/')
    setup_driver.maximize_window()
    assert setup_driver.find_element_by_css_selector('h1').text == "Hello World"