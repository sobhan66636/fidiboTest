import pytest
from selenium import webdriver
import os
import shutil

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    
    # 1. Add critical arguments to avoid DevToolsActivePort errors
    options.add_argument("--no-sandbox")  # Essential for Docker/CI environments
    options.add_argument("--disable-dev-shm-usage")  # Fixes limited resource issues
    options.add_argument("--remote-debugging-port=9222")  # Explicit port for DevTools
    
    # 2. Clean up or validate the user-data-dir
    user_data_dir = "fidibo_chromium"
    if os.path.exists(user_data_dir):
        # Clear existing profile (or skip this if you want persistent data)
        shutil.rmtree(user_data_dir, ignore_errors=True)
    os.makedirs(user_data_dir, exist_ok=True)
    options.add_argument(f"user-data-dir={user_data_dir}")

    # 3. Initialize driver with error handling
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        pytest.fail(f"Failed to initialize Chrome driver: {str(e)}")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()