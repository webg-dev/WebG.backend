from pathlib import Path

import geckodriver_autoinstaller
from selenium import webdriver

from utils.io_funcs import read_text_file


class WebDriver():

    def __init__(self):
        geckodriver_autoinstaller.install()
        self.driver = webdriver.Firefox()

    def load_page(self, url: str):
        self.driver.get(url)

    def get_html_dom(self):
        return self.driver.page_source

    def get_screenshot(self):
        return self.driver.get_screenshot_as_base64()

    def get_graph(self):
        build_graph_script_path = Path(__file__).resolve().parent / 'build_graph.js'
        build_graph_script = read_text_file(str(build_graph_script_path))
        self.driver.execute_script(build_graph_script)
        graph = self.driver.execute_script(f'return graph;')
        return graph


if __name__ == '__main__':

    _webdriver = WebDriver()
    _webdriver.load_page('https://www.allbirds.co.uk/products/mens-tree-dashers')
    _graph = _webdriver.get_graph()
    print(_graph)
