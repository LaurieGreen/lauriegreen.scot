import pytest;

def test_title(setup_driver):
    setup_driver.get('http://lauriegreen.scot/')
    setup_driver.maximize_window()
    assert "Laurie Green" in setup_driver.title
    
def test_header(setup_driver):
    setup_driver.get('http://lauriegreen.scot/')
    setup_driver.maximize_window()
    assert setup_driver.find_element_by_css_selector('h1').text == "Hello World"

def test_open_gen(setup_driver):
    setup_driver.get('http://lauriegreen.scot/')
    setup_driver.maximize_window()
    assert setup_driver.find_element_by_css_selector('a[href="gen.html"').text == "Generator"
    setup_driver.find_element_by_css_selector('a[href="gen.html"').click()
    assert setup_driver.current_url == 'http://lauriegreen.scot/gen.html'