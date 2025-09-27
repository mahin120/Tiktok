from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def main():
    # Setup headless Chrome for Termux or desktop
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Remove if you want to see the browser
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Error starting Chrome WebDriver: {e}")
        sys.exit(1)

    try:
        print("=== TikTok View & Like Automation Bot ===")
        video_url = input("Enter TikTok video URL: ").strip()
        if not video_url.startswith("http"):
            print("Invalid URL. Exiting.")
            sys.exit(1)

        views_count = input("Enter number of views to simulate (max 100): ").strip()
        likes_count = input("Enter number of likes to send (max 50): ").strip()

        try:
            views_count = int(views_count)
            likes_count = int(likes_count)
        except ValueError:
            print("Invalid number entered. Exiting.")
            sys.exit(1)

        if views_count < 0 or views_count > 100 or likes_count < 0 or likes_count > 50:
            print("Numbers out of allowed ranges. Exiting.")
            sys.exit(1)

        print("Opening TikTok video page...")
        driver.get(video_url)
        time.sleep(5)  # Wait page load

        # Simulate views by refreshing the page multiple times
        print(f"Simulating {views_count} views by refreshing...")
        for i in range(views_count):
            driver.refresh()
            time.sleep(2)
            print(f"View {i+1}/{views_count} done")

        # Try to find the Like button and click likes_count times
        print(f"Attempting to click like button {likes_count} times...")
        # Like button XPath may vary; this is a common xpath for TikTok like button on desktop site
        try:
            like_button = driver.find_element(By.XPATH, '//span[contains(@data-e2e, "like-icon")]')
        except Exception as e:
            print("Could not find like button, exiting.")
            driver.quit()
            sys.exit(1)

        for i in range(likes_count):
            try:
                like_button.click()
                print(f"Clicked like {i+1}/{likes_count}")
                # Usually TikTok prevents repeated likes, so this is symbolic
                time.sleep(2)
            except Exception as e:
                print(f"Failed to click like at {i+1}: {e}")
                break

        print("Task complete. Exiting.")
        driver.quit()

    except Exception as general_error:
        print(f"An error occurred: {general_error}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()