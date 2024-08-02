import argparse
import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

import logging

logging.basicConfig(level=logging.INFO)

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

        def to_filename(page_title: str):
            words = page_title.split()
            prefix = words[-1]
            suffix = " ".join(words[:words.index("-")])
            result = f"{prefix} {suffix}".replace(" ", "_").lower()
            return f"{result}_{datetime.datetime.now()}.html"
            
        title = page.title()
        _logger.debug(f"page title: {title}")

        soup = BeautifulSoup(page.content(), "html.parser")
        _logger.debug(soup.prettify())

        path = Path(to_filename(title))
        with open(path, "w") as html:
            _logger.info(f"writing html content to: {path.absolute()}")
            html.write(soup.prettify())
            #TODO: return file bytestream to support XCOM pull in downstream crawler task

        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="zoopla-page-renderer", 
        description="renders dynamic and static html content."
    )

    parser.add_argument("url", help="url")
    args = parser.parse_args()
    
    main(url = args.url)

