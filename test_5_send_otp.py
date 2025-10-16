import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@allure.epic("Login")
@allure.feature("Send OTP Code")
def test_5_send_otp(driver):
    phone_number_box_selector = (By.CLASS_NAME, "phone-input-field")
    phone_country_selector = (By.CLASS_NAME, "phone-input-country")
    login_button_selector = (By.CLASS_NAME, "login-box-submit")

    wait = WebDriverWait(driver, 10)
    driver.get('https://fidibo.com/login')

    country = wait.until(EC.visibility_of_element_located(phone_country_selector))
    phonebox = wait.until(EC.visibility_of_element_located(phone_number_box_selector))
    login_button = wait.until(EC.visibility_of_element_located(login_button_selector))

    wait.until(EC.element_to_be_clickable(country))

    with allure.step("Enter phone number and click login"):
        phonebox.send_keys('9385198683')
        login_button.click();
        input_selector = (By.NAME, "otp")
        input = wait.until(EC.visibility_of_element_located(input_selector))
        assert input.is_displayed(), "OTP Code must be sent and OTP input must be displayed"


        
