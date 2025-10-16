import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

test_shelf_name = 'مار زرد و آبی'

@allure.epic("Library")
@allure.feature("Delete a shelf")
def test_remove_shelf(driver):
    driver.get('https://fidibo.com/library/book/shelves')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Create a new shelf'):
        row_button_container = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'page-options-header-main-buttons-section-grid')))
        row_button = row_button_container.find_elements(By.TAG_NAME, 'button')[0]
        row_button.click();
        shelves_container = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shelve-card-container')))
        add = shelves_container.find_element(By.CLASS_NAME, 'add')
        add.click()
        name = wait.until(EC.element_to_be_clickable((By.NAME, 'name')))  
        name.send_keys(test_shelf_name)
        confirm_shelf = driver.find_element(By.CLASS_NAME, 'add-shelve-btn')
        confirm_shelf.click()
        assert wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shelve-card-container"), test_shelf_name)), "New shelf item must appear"

    with allure.step('Delete the created shelf'):
        shelf = shelves_container.find_elements(By.CLASS_NAME, 'shelve-card-row')[1]
        driver.get(shelf.get_property('href'))
        delete = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shelve-page-buttons-delete')))
        delete.click()
        confirm_delete = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'alert-modal-submit')))
        confirm_delete.click();
        assert wait.until(EC.url_to_be('https://fidibo.com/library/book/shelves')), "Must redirect out when sucessfully deleted"


