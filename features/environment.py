"""Behave hooks: start and stop the browser, screenshot on failure."""
from pathlib import Path

from utils.driver_factory import create_driver

SCREENSHOT_DIR = Path("screenshots")


def before_scenario(context, scenario):
    context.driver = create_driver()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        SCREENSHOT_DIR.mkdir(exist_ok=True)
        name = scenario.name.replace(" ", "_")[:50]
        context.driver.save_screenshot(str(SCREENSHOT_DIR / f"{name}.png"))
    context.driver.quit()