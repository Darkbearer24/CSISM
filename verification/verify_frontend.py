from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the local server
        page.goto("http://localhost:5173", timeout=60000)

        # Wait for the React app to mount and render the Hero section
        # We look for the h1 in the hero section
        hero_heading = page.locator(".hero h1")
        expect(hero_heading).to_be_visible(timeout=10000)

        # Verify content matches expectations
        expect(page.get_by_text("Professional Guidance for ISM College Establishment")).to_be_visible()

        # Scroll down to ensure all lazy loaded content (if any) or just to show the page in screenshot
        # We'll take a full page screenshot

        # Take screenshot
        page.screenshot(path="verification/landing_page.png", full_page=True)

        print("Verification successful, screenshot saved.")
        browser.close()

if __name__ == "__main__":
    run()
