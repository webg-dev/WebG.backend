from pathlib import Path
from time import time, sleep
from typing import Optional

import geckodriver_autoinstaller
from selenium import webdriver
from xvfbwrapper import Xvfb

from models import WebPage, Graph
from utils.io_funcs import read_text_file


class WebDriver:

    def __init__(self,
                 use_virtual_display: Optional[bool] = False,
                 viewport_width: Optional[int] = 1500,
                 viewport_height: Optional[int] = 3000):
        print('Initialising Webdriver...')
        geckodriver_autoinstaller.install()
        self.use_virtual_display = use_virtual_display
        self.vdisplay = None

        # Open Browser
        if self.use_virtual_display:
            self.setup_virtual_display(viewport_width=viewport_width, viewport_height=viewport_height)
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(viewport_width, viewport_height)
        self.viewport_width = self.driver.execute_script('return window.innerWidth;')
        self.viewport_height = self.driver.execute_script('return window.innerHeight;')

    def setup_virtual_display(self, viewport_width: int, viewport_height: int) -> None:
        self.vdisplay = Xvfb(width=viewport_width, height=viewport_height, colordepth=24)
        self.vdisplay.start()

    def load_page(self, url: str, timeout: Optional[float] = 10) -> None:
        print(f'Loading: {url}')
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

    def get_web_page(self, url: str) -> WebPage:
        self.load_page(url)
        web_page = WebPage(
            url=self.driver.current_url,
            viewportWidth=self.viewport_width,
            viewportHeight=self.viewport_height,
            html=self.get_html_dom(),
            screenshot=self.get_screenshot(),
            graph=self.get_graph()
        )

        return web_page

    def quit(self):
        self.driver.quit()
        if self.use_virtual_display:
            self.vdisplay.stop()
