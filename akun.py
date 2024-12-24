from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Lokasi ChromeDriver
driver = webdriver.Chrome(executable_path='https://developer.chrome.com/docs/chromedriver/downloads?hl=id#chromedriver_1140573590')

# Buka halaman bantuan Instagram
driver.get("https://www.instagram.com/hacked")

# Isi formulir
try:
    email_field = driver.find_element(By.NAME, "jalanjalanmalam248")
    email_field.send_keys("jalanjalanmalam248")
    email_field.send_keys(Keys.RETURN)

    print("Formulir telah diisi. Tunggu konfirmasi dari Instagram.")
except Exception as e:
    print("Terjadi kesalahan:", e)

# Tutup browser
driver.quit()