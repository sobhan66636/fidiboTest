import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@allure.epic("Home Page")
@allure.feature("Load Active Sessions")
def test_active_sessions(driver):
    driver.get('https://fidibo.com/profile/account')
    wait = WebDriverWait(driver, 10)
    with allure.step('Enter active sessions through account page'):
        sidebar_buttons = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile-side-buttons')))
        sessions = sidebar_buttons.find_elements(By.TAG_NAME, 'a')[3]
        sessions.click();
        items = wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'devices-page-content-box-content-item')))
        assert len(items) > 0, "Active session items must have at least 1 item"



