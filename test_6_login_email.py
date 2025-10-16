import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.epic("Login")
@allure.feature("Login using email address")
def test_6_login_email(driver):
    driver.get('https://fidibo.com/login/email')
    email_selector = (By.NAME, "email")
    password_selector = (By.CLASS_NAME, "password")
    login_selector = (By.CLASS_NAME, "login-box-submit")
    wait = WebDriverWait(driver, 10)

    with allure.step('Enter email address'):
        email = wait.until(EC.visibility_of_element_located(email_selector))
        email.send_keys('fidibotest50@gmail.com')

        login = wait.until(EC.element_to_be_clickable(login_selector))  # Ensure button is clickable
        login.click()

        password = wait.until(EC.visibility_of_element_located(password_selector))
        assert password.is_displayed()  # Ensure password field appears

    with allure.step('Enter password'):
        password.send_keys('Test123456789!')
        
        password_login = driver.find_elements(By.CLASS_NAME, 'login-box-submit')[1]
        password_login.click()
        assert wait.until(EC.url_to_be('https://fidibo.com/')), "Must redirect to home page after successful login"
