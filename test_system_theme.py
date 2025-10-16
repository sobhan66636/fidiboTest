import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@allure.epic("Home Page")
@allure.feature("Set system theme mode")
def test_system_theme(driver):
    driver.get('https://fidibo.com')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    theme_selector = (By.CLASS_NAME, 'header-theme-btn')
    is_system_dark = driver.execute_script("return window.matchMedia('(prefers-color-scheme: dark)').matches;")

    
    with allure.step('Click theme button'):
        theme = wait.until(EC.element_to_be_clickable(theme_selector))
        theme.click()
        

    with allure.step('Click system theme mode'):
        light_mode = driver.find_elements(By.CLASS_NAME, 'header-top-user-menu-item')[2]
        light_mode.click()
        background = driver.find_element(By.CLASS_NAME, 'home-page')
        matches_system = False;
        if is_system_dark:
            matches_system = background.value_of_css_property('background-color') == 'rgba(35, 33, 31, 1)'
        else:
            matches_system = background.value_of_css_property('background-color') == 'rgba(248, 245, 241, 1)'
        assert matches_system, "Background color must be set to system theme color"