import time
from selenium.common import ElementClickInterceptedException


def wait_for_click_not_intercepted(element, retry_count=5):
    for i in range(retry_count):
        try:
            return element.click()
        except ElementClickInterceptedException:
            time.sleep(1)
