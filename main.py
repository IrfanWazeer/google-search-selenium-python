import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import atexit

# Make screenshots directory if not exists
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Launch Chrome (compatible with Chrome v137)
driver = uc.Chrome(version_main=137)

# Ensure browser closes safely on exit
atexit.register(lambda: safe_quit(driver))

def safe_quit(driver):
    try:
        driver.quit()
    except Exception:
        pass

try:
    # Step 1: Open Google
    driver.get("https://www.google.com")

    # Step 2: Wait for search box
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Step 3: Type like human
    query = "Selenium Python"
    for char in query:
        search_box.send_keys(char)
        time.sleep(0.2)

    search_box.send_keys(Keys.RETURN)

    # Step 4: Wait for first search result
    first_result = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h3'))
    )

    # Step 5: Click on first result
    first_result.click()

    # Step 6: Wait for page to load completely
    WebDriverWait(driver, 20).until(lambda d: d.title != "")

    # Step 7: Print and save details
    print("✅ Page Title:", driver.title)
    print("🌐 Page URL:", driver.current_url)

    # Step 8: Save screenshot
    screenshot_path = os.path.join(screenshot_dir, "result_page.png")
    driver.save_screenshot(screenshot_path)
    print(f"📸 Screenshot saved at: {screenshot_path}")

except Exception as e:
    print("⚠️ Something went wrong:", e)
