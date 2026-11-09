import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load the local index.html
        await page.goto('file:///app/index.html')

        # Wait for map canvases to load
        await page.wait_for_selector('canvas.multi-canvas')

        # Move mouse over a canvas
        canvas = await page.query_selector('canvas.multi-canvas')
        box = await canvas.bounding_box()

        if box:
            await page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)

            # Check tooltip visibility and content
            await page.wait_for_selector('.tip', state='visible')

            # Since the layout may be updated asynchronously, wait a bit
            await asyncio.sleep(0.5)

            tooltip = await page.query_selector('.tip')
            tooltip_text = await tooltip.inner_text()

            print(f"Tooltip is visible: {await tooltip.is_visible()}")
            print(f"Tooltip text:\n{tooltip_text}")

            if '°N' in tooltip_text and '°E' in tooltip_text:
                print("Test passed: Tooltip contains expected coordinates.")
            else:
                print("Test failed: Tooltip content does not match expected format.")
        else:
            print("Canvas not found or not visible")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
