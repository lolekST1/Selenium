""" łączenie ze stroną za pomocą drivera, prosta interakcja ze stroną """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH = "D:\OneDrive\Elektronika\Programowanie\Testowanie\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://wodzirejkarol.pl/blog-wodzireja/")
print(driver.title)  # drukuje tytuł strony
search = driver.find_element_by_name("s")  # szuka elementu
search.send_keys("jak zepsuć")  # wpisuje tekst
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fl-page-content"))
    )  # czeka na pojawienie się elementu
    articles = main.find_elements_by_tag_name("article")  # szuka wszystkich elementów z tagiem "article"
    for a in articles:
        header = a.find_element_by_class_name("fl-post-title")  # wyszukuje nagłówków i je drukuje
        print(header.text)
finally:
    driver.quit()  # ostatecznie zamyka program

# print((driver.page_source))                           # drukuje kod źródłowy
