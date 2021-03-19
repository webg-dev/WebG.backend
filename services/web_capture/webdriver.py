from pathlib import Path
from time import time, sleep
from typing import Optional

import geckodriver_autoinstaller
from selenium import webdriver

from utils.io_funcs import read_text_file


class WebDriver:

    def __init__(self):
        geckodriver_autoinstaller.install()
        self.driver = webdriver.Firefox()

    def load_page(self, url: str, timeout: Optional[float] = 10) -> None:
        self.driver.get(url)
        self._wait_for_page_load(timeout)

    def _wait_for_page_load(self, timeout: float) -> None:
        """Waits for page to fully load by checking each second
        whether any new nodes have been added to the DOM."""
        start_time = time()
        previous_num_elements = 0
        while time() - start_time < timeout:
            num_elements = len(self.driver.find_elements_by_css_selector('*'))
            if num_elements > previous_num_elements:
                previous_num_elements = num_elements
                sleep(1)
            else:
                break


    def get_html_dom(self) -> str:
        return self.driver.page_source

    def get_screenshot(self) -> str:
        return self.driver.get_screenshot_as_base64()

    def get_graph(self) -> dict:
        script_path = Path(__file__).resolve().parent / 'build_graph.js'
        script = read_text_file(str(script_path))
        self.driver.execute_script(script)
        graph = self.driver.execute_script(f'return graph;')
        return graph


if __name__ == '__main__':

    _webdriver = WebDriver()
    _webdriver.load_page('https://amazon.co.uk')
    _graph = _webdriver.get_graph()
    print(len(_graph['nodes']))
    sleep(5)
    _graph = _webdriver.get_graph()
    print(len(_graph['nodes']))
