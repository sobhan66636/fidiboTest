import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.epic("Product Page")
@allure.feature("Audio book sample")
def test_audio_book_sample(driver):
    driver.get('https://fidibo.com/book/86020-%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B5%D9%88%D8%AA%DB%8C-%D9%85%D9%84%D8%AA-%D8%B9%D8%B4%D9%82')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Click sample'):
        sample = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'book-buy-box-footer-second')))
        sample.click()
        audio_player = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'audio-player')))
        assert audio_player.is_displayed(), "Audio player must appear after clicking sample"

    with allure.step('Close audio player'):
        close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'audio-player-content-close')))
        close.click()
        wait.until(EC.staleness_of(audio_player))

    
    


