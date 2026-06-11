from playwright.async_api import async_playwright


class PlaywrightConnector:

    async def get_page_content(
        self,
        url: str
    ):

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=True
            )

            page = await browser.new_page()

            await page.goto(
                url,
                wait_until="domcontentloaded"
            )

            content = await page.content()

            await browser.close()

            return content