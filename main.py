from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
service = Service()  # Sesuaikan path chromedriver kalau perlu
driver = webdriver.Chrome(service=service, options=options)

# Buka URL
driver.get("https://open-brew.vercel.app/")
wait = WebDriverWait(driver, 10)

# Tunggu dan klik tombol menu "KYC Addresses"
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(.,'KYC Addresses')]]"))).click()
time.sleep(2)

# CSV setup
csv_with_number = open("tea_kyc_addresses_with_number.csv", "w", newline="", encoding="utf-8")
csv_without_number = open("tea_kyc_addresses.csv", "w", newline="", encoding="utf-8")
writer_with_number = csv.writer(csv_with_number)
writer_without_number = csv.writer(csv_without_number)
writer_with_number.writerow(["No", "Address"])
writer_without_number.writerow(["Address"])

total_data = 0
page_count = 1

while True:
    # Scroll dalam 1 halaman biar semua data muncul
    for _ in range(6):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)

    # Ambil semua address yang terlihat
    items = driver.find_elements(By.CSS_SELECTOR, "li.address-components_addressItem__yYlDS")
    for item in items:
        try:
            address_span = item.find_element(By.CSS_SELECTOR, "span.address-components_addressText__Th_Zi")
            address = address_span.get_attribute("data-address")
            total_data += 1
            writer_with_number.writerow([f"{total_data}. {address}"])
            writer_without_number.writerow([address])
        except Exception as e:
            print("Gagal ambil address:", e)

    print(f"✅ Page {page_count} selesai. Total address: {total_data}")

    # Cek tombol Next
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, "button.address-components_paginationBtn__UGqyW")
        if next_btn.is_enabled():
            next_btn.click()
            page_count += 1
            time.sleep(2)
        else:
            break
    except:
        break

# Tutup file dan browser
csv_with_number.close()
csv_without_number.close()
driver.quit()

print(f"Selesai! Total {total_data} address disimpan ke dua file CSV.")
