import pytest;

@pytest.fixture()
def setup_driver():
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	yield driver
	driver.close()

def test_title(setup_driver):
    setup_driver.get('http://lauriegreen.scot/')
    setup_driver.maximize_window()
    assert "Laurie Green" in setup_driver.title
    
def test_header(setup_driver):
    setup_driver.get('http://lauriegreen.scot/')
    setup_driver.maximize_window()
    assert setup_driver.find_element_by_css_selector('h1').text == "Hello World"