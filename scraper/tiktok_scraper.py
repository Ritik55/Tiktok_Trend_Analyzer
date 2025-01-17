import asyncio
from playwright.async_api import async_playwright

class TikTokScraper:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None

    async def initialize(self):
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def scrape_trending_data(self):
        await self.page.goto("https://www.tiktok.com/trending")
        await self.page.wait_for_selector(".video-feed-item")
        
        trending_data = await self.page.evaluate("""
            () => {
                const items = document.querySelectorAll('.video-feed-item');
                return Array.from(items).map(item => ({
                    username: item.querySelector('.user-username').innerText,
                    description: item.querySelector('.video-desc').innerText,
                    likes: item.querySelector('.like-count').innerText,
                    comments: item.querySelector('.comment-count').innerText,
                    shares: item.querySelector('.share-count').innerText
                }));
            }
        """)
        
        return trending_data

    async def close(self):
        await self.browser.close()

async def main():
    scraper = TikTokScraper()
    await scraper.initialize()
    trending_data = await scraper.scrape_trending_data()
    print(trending_data)
    await scraper.close()

if __name__ == "__main__":
    asyncio.run(main())
