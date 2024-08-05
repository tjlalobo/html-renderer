import argparse

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

import logging

logging.basicConfig(level=logging.DEBUG)

_logger = logging.getLogger(f"html-renderer.{__name__}")

def main(url: str):
    _logger.info(f"rendering html: URL: {url}")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(slow_mo=1000)
        context = browser.new_context(
            user_agent="Chrome/51.0.2704.103 Safari/537.36" #TODO: configure
        )
        
        page = context.new_page()
        page.goto(url)
            
        title = page.title()
        _logger.debug(f"page title: {title}")

        soup = BeautifulSoup(page.content(), "html.parser")
        _logger.debug(soup.prettify())
        
        #TODO: return map of page to file bytestreams

        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="html-renderer", 
        description="renders dynamic and static html content."
    )

    parser.add_argument("url", help="url")
    args = parser.parse_args()
    
    main(url = args.url)

