"""Creates the WebDriver based on the browser set in config.ini."""
from selenium import webdriver

from utils import config_reader


def create_driver():
    browser = config_reader.get("app", "browser").lower()
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
    raise ValueError(f"Unsupported browser: {browser}")