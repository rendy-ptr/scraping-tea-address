# 🧹 OpenBrew Address Scraper

Tool sederhana untuk scraping alamat wallet dari menu **KYC Addresses** di [OpenBrew Explorer](https://open-brew.vercel.app/). Scraper ini otomatis scroll halaman, klik tombol **Next** jika ada, dan menyimpan seluruh hasil ke dua file CSV.

---

## 🌐 Sumber Data

Data diambil dari halaman:  
🔗 [https://open-brew.vercel.app/](https://open-brew.vercel.app/)  
Bagian: **KYC Addresses**

---

## 📦 Fitur

- ✅ Otomatis scroll sampai semua data tampil  
- ✅ Klik otomatis tombol **Next**  
- ✅ Simpan ke dua file CSV:
  - addresses_with_number.csv → dengan nomor urut (1. address)
  - addresses.csv → hanya address

---

## 🔧 Kebutuhan

- Python 3.7+
- Google Chrome
- Python packages:
  - selenium
  - webdriver-manager

---

# Panduan Menjalankan Proyek

## 🚀 Cara Menjalankan
1. **Install dependencies terlebih dahulu**
   ```bash
   pip install selenium webdriver-manager
   ```

2. **Jalankan proyek**
   ```bash
   python main.py
   ```
