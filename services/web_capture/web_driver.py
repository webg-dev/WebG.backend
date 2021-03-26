from pathlib import Path
from time import time, sleep
from typing import Optional

import geckodriver_autoinstaller
from selenium import webdriver
from xvfbwrapper import Xvfb

from utils.io_funcs import read_text_file
from models import WebPage, Graph


class WebDriver:

    def __init__(self,
                 use_virtual_display: Optional[bool] = False,
                 viewport_width: Optional[int] = 1500,
                 viewport_height: Optional[int] = 3000):
        geckodriver_autoinstaller.install()
        self.use_virtual_display = use_virtual_display
        self.vdisplay = None
        if self.use_virtual_display:
            self.setup_virtual_display()
        self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        self.driver.set_window_size(1500, 3000)

    def setup_virtual_display(self) -> None:
        """Setup a virtual display with xvfb

        We cannot run headless chrome with extensions enabled thus run the gui in a virtual framebuffer.
        Chromium behaves the same as google chrome in this respect.

        Untested on how this code would behave if there were more than one xvfb instances.
        """
        self.vdisplay = Xvfb(width=1500, height=3000, colordepth=24)
        self.vdisplay.start()

    def load_page(self, url: str, timeout: Optional[float] = 10) -> None:
        self.driver.get(url)
        self._wait_for_page_load(timeout)

    def _wait_for_page_load(self, timeout: float) -> None:
        """Waits for page to fully load by checking each second
        whether any new nodes have been added to the DOM."""
        start_time = time()
        previous_num_elements = 0
        while True:
            num_elements = len(self.driver.find_elements_by_css_selector('*'))
            if num_elements > previous_num_elements:
                print(f'{num_elements - previous_num_elements} new nodes were added...')
                previous_num_elements = num_elements
                sleep(1)
            else:
                print(f'Page fully loaded with {num_elements} elements')
                break

            if time() - start_time > timeout:
                print(f'Page load timeout {timeout}s reached')
                break

    def get_html_dom(self) -> str:
        return self.driver.page_source

    def get_screenshot(self) -> str:
        return self.driver.get_screenshot_as_base64()

    def get_graph(self) -> Graph:
        script_path = Path(__file__).resolve().parent / 'build_graph.js'
        script = read_text_file(str(script_path))
        self.driver.execute_script(script)
        graph = self.driver.execute_script('return graph;')
        graph = Graph(**graph)
        print(f'Constructed graph with {len(graph.nodes)} nodes.')
        return graph


if __name__ == '__main__':
    start = time()
    _webdriver = WebDriver(headless=True)
    url = 'file:////home/luka/Downloads/Matcha Hemp Hydrating Cleanser _ Cleanser For Sensitive Skin – KraveBeauty (23_02_2021 17_11_07).html'
    _webdriver.load_page(url)
    _graph = _webdriver.get_graph()
    _html = _webdriver.get_html_dom()
    _screenshot = _webdriver.get_screenshot()
    _webdriver.stop_virtual_display()
    print(f'Constructed graph with {len(_graph["nodes"])} nodes in {time() - start:.2f}s')
    from pprint import pprint

    pprint(_graph)
