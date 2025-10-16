import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@allure.epic("Login")
@allure.feature("Phone Validation")
def test_2_phone_validation(driver):
    phone_number_box_selector = (By.CLASS_NAME, "phone-input-field")
    phone_country_selector = (By.CLASS_NAME, "phone-input-country")
    login_button_selector = (By.CLASS_NAME, "login-box-submit")

    wait = WebDriverWait(driver, 10)
    driver.get('https://fidibo.com/login')

    country = wait.until(EC.visibility_of_element_located(phone_country_selector))
    phonebox = wait.until(EC.visibility_of_element_located(phone_number_box_selector))
    login_button = wait.until(EC.visibility_of_element_located(login_button_selector))

    wait.until(EC.element_to_be_clickable(country))

    with allure.step("Enter invalid phone number"):
        phonebox.send_keys('1234')
        assert not login_button.is_enabled(), "Login button should be disabled for invalid input"

    with allure.step("Enter valid phone number"):
        phonebox.clear()
        phonebox.send_keys('9981991407')
        assert login_button.is_enabled(), "Login button should be enabled for valid input"
