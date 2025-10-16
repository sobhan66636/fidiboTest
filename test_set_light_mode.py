import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@allure.epic("Home Page")
@allure.feature("Set light mode")
def test_set_light_mode(driver):
    driver.get('https://fidibo.com')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    theme_selector = (By.CLASS_NAME, 'header-theme-btn')
    
    with allure.step('Click theme button'):
        theme = wait.until(EC.element_to_be_clickable(theme_selector))
        theme.click()
        

    with allure.step('Click light mode button'):
        light_mode = driver.find_elements(By.CLASS_NAME, 'header-top-user-menu-item')[0]
        light_mode.click()
        background = driver.find_element(By.CLASS_NAME, 'home-page')
        assert background.value_of_css_property('background-color') == 'rgba(248, 245, 241, 1)', "Background color must be set to light color"
   

    
    


