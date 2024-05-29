import pytest
from selenium import webdriver
from config import URL

@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.get(f'{URL}')
    yield firefox
    firefox.quit()