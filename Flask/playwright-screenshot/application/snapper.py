"""Snapper class from Playwright"""

import base64
import os

from playwright.sync_api import sync_playwright


class PlaywrightSnapper(object):
    def __init__(self, render_html:bool=True) -> None:
        self.render_html = render_html

    def process_snapshot(self, pages:list) -> list:
        """Take snapshot of pages in a batch (playwright)"""

        try:
            with sync_playwright() as pw:
                self.browser = pw.chromium.launch()
                self.context = self.browser.new_context(
                    ignore_https_errors=True,
                )

                self.page = self.context.new_page()
                for page in pages:

                    if self.render_html:
                        self.page.set_content(page.get("page_content"))
                        del page["page_content"]
                    else:
                        self.page.goto(page.get("page_url"))
                        del page["page_url"]

                    self.page.set_viewport_size(
                        {
                            "width": page.get("page_width"),
                            "height": page.get("page_height")
                        }
                    )

                    b64_content = self.page.screenshot(full_page=page.get("full_page"))
                    page["base64_content"] = base64.b64encode(b64_content).decode()

                return pages

        except Exception as error:
            print("Service Status: Snapshot failed with error: ", error)
            return pages
