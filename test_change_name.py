import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random;
names = ['امیر', 'بهرام', 'پریسا', 'تیمور', 'ثریا', 'جمشید', 'چنار', 'حمید', 'خیار', 'دنیا', 'ذغال', 'رها']


@allure.epic("Home Page")
@allure.feature("Change profile name")
def test_change_name(driver):
    driver.get('https://fidibo.com/profile/account')
    wait = WebDriverWait(driver, 10)
    with allure.step('Set new name'):
        name_selector = (By.NAME, 'first_name')
        name = wait.until(EC.visibility_of_element_located(name_selector))
        name.clear();
        name.send_keys(random.choice(names));
    
    with allure.step('Click confirmation button'):
        confirmation = driver.find_element(By.CLASS_NAME, 'profile-content-section-submit-btn')
        confirmation.click()
        wait.until(EC.url_changes(driver.current_url))
        assert driver.current_url.endswith('overview'), "Must redirect to profile page if name was changed successfully"

    
    


