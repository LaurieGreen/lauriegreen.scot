import pytest;

def test_opening_gen_from_homepage(setup_driver):
    setup_driver.get('http://lauriegreen.scot/')
    setup_driver.maximize_window()
    assert setup_driver.find_element_by_css_selector('a[href="gen.html"').text == "Generator"
    setup_driver.find_element_by_css_selector('a[href="gen.html"').click()
    assert setup_driver.current_url == 'http://lauriegreen.scot/gen.html'

def test_gif_button(setup_driver):
 	setup_driver.get('http://lauriegreen.scot/gen.html')
	setup_driver.maximize_window()
	assert setup_driver.find_element_by_css_selector('img[id="gifholder"').get_attribute("src") == "http://i.imgur.com/pg5qRqS.gif"
	setup_driver.find_element_by_css_selector('button[id="readButton"').click()
	assert setup_driver.find_element_by_css_selector('img[id="gifholder"').get_attribute("src") != "http://i.imgur.com/pg5qRqS.gif"