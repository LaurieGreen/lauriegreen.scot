import pytest;
import requests;

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

def test_image_source():
	url = 'http://lauriegreen.scot/read.php'
	headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
	'Connection': 'keep-alive',
	'Host': 'lauriegreen.scot',
	'Upgrade-Insecure-Requests': '1'
	}
	result = requests.get(url, headers=headers)
	urls = result.json()
	for url in urls:
		response = requests.get(url)
		assert response.status_code == 200
