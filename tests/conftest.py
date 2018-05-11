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