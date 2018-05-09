import pytest;
from selenium import webdriver;

driver = webdriver.Chrome();

def test_title():
    driver.get('http://lauriegreen.scot/')
    driver.maximize_window()
    assert "Laurie Green" in driver.title
    driver.close()
    

def test_header():
    driver.get('http://lauriegreen.scot/')
    driver.maximize_window()
    assert driver.find_element_by_css_selector('h1').text == "Hello World"
    driver.close()