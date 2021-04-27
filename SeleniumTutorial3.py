""" Wypełnia formularz kontaktowy na stronie """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH = "D:\OneDrive\Elektronika\Programowanie\Testowanie\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://wodzirejkarol.pl/blog-wodzireja/")
print(driver.title)  # drukuje tytuł strony
link = driver.find_element_by_link_text("Kontakt")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wpcf7-f55-p16-o1"))
    )
    e = driver.find_element_by_name("your-name")
    e.send_keys("Karol Stolarski")
    e = driver.find_element_by_name("your-email")
    e.send_keys("lolekst@gmail.com")
    e = driver.find_element_by_name("your-message")
    e.send_keys("Testowanie selenium")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "acceptance-219"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".wpcf7-submit"))
    )
    element.click()
    driver.back()
finally:
    driver.quit()
