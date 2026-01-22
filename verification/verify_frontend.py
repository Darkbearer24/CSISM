from playwright.sync_api import sync_playwright
import os

def verify_js_extraction():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # Check if the script tag is present
        script = page.locator('script[src="static/js/app.js"]')
        if script.count() > 0:
            print("Script tag found!")
        else:
            print("Script tag NOT found!")
            exit(1)

        # Check if the form exists
        form = page.locator("#enquiryForm")
        if form.count() > 0:
            print("Form found!")
        else:
            print("Form NOT found!")
            exit(1)

        # Ensure directory exists
        os.makedirs("verification", exist_ok=True)
        page.screenshot(path="verification/frontend_verification.png")
        print("Screenshot taken.")
        browser.close()

if __name__ == "__main__":
    verify_js_extraction()
